from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


CHROME_EXEC_PATH = "C:/Users/T852/DeveloperFoo/chromedriver_win32/chromedriver.exe"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0
        self.servicer = webdriver.chrome.service.Service(CHROME_EXEC_PATH)
        self.driver = webdriver.Chrome(service=self.servicer)

    def get_internet_speed(self):
        URL = "https://www.speedtest.net"
        self.driver.get(URL)
        go_button_we = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'start-text')))
        go_button_we.click()
        time.sleep(30)
        down_we = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')))
        print(f'down: "{down_we.text}"')
        self.down = float(down_we.text)
        print(self.down)

        time.sleep(20)
        up_we = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'upload-speed')))
        print(f'up: "{up_we.text}"')
        self.up = float(up_we.text)
        print(self.up)
        #Quit Driver
        # self.driver.quit()


    def tweet_at_provider(self):
        URL = "https://www.twitter.com"
        self.driver.get(URL)

