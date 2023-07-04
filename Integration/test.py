import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the webdriver
driver = webdriver.Chrome()

# YouTube website
driver.get("https://www.youtube.com/")


try:
    # Test 1: search query
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="search"]'))
    )
    search_input.send_keys("Basketball")
    search_input.submit()
    time.sleep(5)
    # Test  2: Click on the first video
    first_video = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="video-title"][1]'))
    )
    first_video.click()
    time.sleep(5)
    # Test 3: Pause the video
    video_player = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//video[@class="video-stream html5-main-video"]'))
    )
    video_player.click()
    time.sleep(5)
    # Test 4: Navigate to the channel of the video
    channel_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@id="upload-info"]//a[@class="yt-simple-endpoint style-scope yt-formatted-string"]'))
    )
    channel_name.click()
    time.sleep(5)

    driver.implicitly_wait(5)

finally:

    driver.quit()
