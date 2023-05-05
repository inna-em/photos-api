import tempfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

#TODO перед вызовом каждой функции авторизоваться


def get_photo_urls(username, max_cnt):
    # Set up the web driver
    driver = webdriver.Chrome('./chromedriver', chrome_options=options)

    # Navigate to the Instagram profile page
    driver.get('https://www.instagram.com/' + username + '/')
    # Wait for the page to load
    time.sleep(2)

    # Collect photo urls while scrolling down to load more photos
    photo_links = []
    last_height = driver.execute_script("return document.body.scrollHeight")
    while len(photo_links) < max_cnt:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        photo_elems = driver.find_elements(By.CSS_SELECTOR, 'a[href]')
        for elem in photo_elems:
            if len(photo_links) == max_cnt:
                break
            link = elem.get_attribute('href')
            if '/p/' in link:
                photo_links.append(link)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Close the browser
    driver.quit()

    # Return resulting urls list
    return photo_links


def upload_photos(photos, caption):
    # Set up the web driver (make sure to have the correct driver executable installed)
    driver = webdriver.Chrome('./chromedriver', chrome_options=options)

    # Navigate to the Instagram login page
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(2)

    username = 'repinyury'
    password = 'Raspberry201190!'

    # Log in with your username and password
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'username'))
    )
    username_field.send_keys(username)
    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    time.sleep(3)

    # Navigate to the upload page
    driver.get('https://www.instagram.com/' + username)

    new_post_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="New post"]'))
    )
    # new_post_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="New post"]')
    new_post_button.click()

    # Upload the photo
    upload_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@type="file"]'))
    )
    # upload_input = driver.find_element(By.XPATH, '//input[@type="file"]')

    content = photos[0].file.read()

    with tempfile.NamedTemporaryFile() as temp_file:
        temp_file.write(content)
        upload_input.send_keys(temp_file.name)
    time.sleep(3)

    post_button = driver.find_element(By.XPATH, '//button[contains(text(), "Next")]')
    post_button.click()
    post_button = driver.find_element(By.XPATH, '//button[contains(text(), "Next")]')
    post_button.click()

    # Add a caption
    caption_input = driver.find_element(By.CSS_SELECTOR, 'textarea[aria-label="Write a caption…"]')
    caption_input.send_keys(caption)

    # Post the photo
    post_button = driver.find_element(By.XPATH, '//button[contains(text(), "Post")]')
    post_button.click()

    # Wait for the upload to complete and close the browser
    time.sleep(5)
    new_post_url = driver.current_url

    driver.quit()

    return new_post_url
