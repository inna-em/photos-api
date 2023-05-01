from selenium import webdriver
import time

# Set up the web driver (make sure to have the correct driver executable installed)
driver = webdriver.Chrome('/path/to/chromedriver')

# Navigate to the Instagram profile page
username = 'username'
driver.get('https://www.instagram.com/' + username + '/')
time.sleep(2)

# Scroll down to load more photos
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
photo_elems = driver.find_elements_by_xpath('//a[@href][@tabindex="-1"]')
for elem in photo_elems:
    link = elem.get_attribute('href')
    if '/p/' in link:
        photo_links.append(link)

# Print the URLs of the photos
print(photo_links)

# Close the browser
driver.quit()