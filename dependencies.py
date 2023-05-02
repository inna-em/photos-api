from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#TODO перед вызовом каждой функции авторизоваться


def get_photo_urls(username, max_cnt):
    # Set up the web driver
    driver = webdriver.Chrome('./chromedriver')

    # Navigate to the Instagram profile page
    driver.get('https://www.instagram.com/' + username + '/')
    time.sleep(2)

    # Scroll down to load more photos
    #TODO подумать, как не скроллить до конца, а считывать фотографии на ходу
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Get the URLs of the photos
    photo_links = []
    for _ in range(max_cnt):
        photo_elems = driver.find_elements(By.CSS_SELECTOR, 'a[href]')
        for elem in photo_elems:
            link = elem.get_attribute('href')
            if '/p/' in link:
                photo_links.append(link)

    # Close the browser
    driver.quit()

    # Return resulting urls list
    return photo_links

# TODO проверить, что для закрытого акка возвращает пустой список


# Set up the web driver (make sure to have the correct driver executable installed)
driver = webdriver.Chrome('./chromedriver')

# Navigate to the Instagram login page
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(2)

# Log in with your username and password
username_field = driver.find_element_by_name('username')
username_field.send_keys('your_username')
password_field = driver.find_element_by_name('password')
password_field.send_keys('your_password')
password_field.send_keys(Keys.RETURN)
time.sleep(2)

# Navigate to the upload page
driver.get('https://www.instagram.com/create')
time.sleep(2)

# Upload the photo
upload_input = driver.find_element(By.XPATH, '//input[@type="file"]')
upload_input.send_keys('/path/to/photo.jpg')
time.sleep(2)

# Add a caption (optional)
caption_input = driver.find_element(By.CSS_SELECTOR, 'textarea[aria-label="Write a caption…"]')
caption_input.send_keys('Caption for the photo')

# Post the photo
post_button = driver.find_element(By.XPATH, '//button[contains(text(), "Post")]')
post_button.click()

# Wait for the upload to complete and close the browser
time.sleep(5)
driver.quit()