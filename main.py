import coding_timer
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import internet_speed_twitter_bot

coding_timer = coding_timer.CodingTimer("time_main.txt")
# coding_timer.start_time()
# coding_timer.pause_time()
# coding_timer.unpause_time()
# coding_timer.stop_time()


DOWN_SPEED_PROMISE = 150
UP_SPEED_PROMISE = 10
# URL = "https://www.twitter.com"
EMAIL_TWITTER = os.environ.get("EMAIL")
PASSWORD_TWITTER = os.environ.get("PASS")
PHONE = os.environ.get("PHONE")

#
# #Create Chrome Driver
# CHROME_EXEC_PATH = "C:/Users/T852/DeveloperFoo/chromedriver_win32/chromedriver.exe"
# servicer = webdriver.chrome.service.Service(CHROME_EXEC_PATH)
# driver = webdriver.Chrome(service=servicer)
#
#
# #Connect Driver to Website
# driver.get(URL)

speed_twitter_bot = internet_speed_twitter_bot.InternetSpeedTwitterBot()
speed_twitter_bot.get_internet_speed()

speed_twitter_bot.tweet_at_provider(DOWN_SPEED_PROMISE, UP_SPEED_PROMISE, EMAIL_TWITTER, PASSWORD_TWITTER, PHONE)
