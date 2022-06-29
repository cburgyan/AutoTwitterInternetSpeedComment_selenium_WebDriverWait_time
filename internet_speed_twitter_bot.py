from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        time.sleep(50)
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

    def tweet_at_provider(self, download_promise, upload_promise, username, password, phone):
        URL = "https://www.twitter.com"
        self.driver.get(URL)
        if self.down < download_promise or self.up < upload_promise:
            try:
                time.sleep(2)
                begin_sign_in_we = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')))
                begin_sign_in_we.click()

                time.sleep(3)
                email_we = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, 'text')))
                email_we.send_keys(username)
                email_we.send_keys(Keys.ENTER)
                try:
                    time.sleep(2.5)
                    phone_we = self.driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
                    phone_we.send_keys(phone)
                    phone_we.send_keys(Keys.ENTER)
                except Exception:
                    pass

                time.sleep(3)
                pass_we = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, 'password')))
                pass_we.send_keys(password)
                pass_we.send_keys(Keys.ENTER)

                time.sleep(5)
                select_emoji_btn_we = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/div[4]/div/div/svg')))
                select_emoji_btn_we.click()
                dissatisfied_emoji_we = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div/div')))
                dissatisfied_emoji_we.click()
                tweet_field2_we = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div')))
                tweet_field2_we.click()
                tweet_field2_we.send_keys(Keys.END)
                tweet_field2_we.send_keys(f'ISP-CompanyX promised a {download_promise}Mbps(downloads) and a {upload_promise}Mbps(uploads) but has only given a {self.down}Mbps(downloads) and a {self.up}Mbps(uploads) according to speedtest.net!!')

                # try:
                #     # click_for_tweeting_we = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[1]/div')))
                #     click_for_tweeting_we = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div')))
                #     click_for_tweeting_we.click()
                #     tweet_field_we = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')))
                #     tweet_field_we.send_keys(f'ISP-CompanyX promised a {download_promise}Mbps(downloads) and a {upload_promise}Mbps(uploads) but has only given a {self.down}Mbps(downloads) and a {self.up}Mbps(uploads) according to speedtest.net!!')
                # except Exception as error_message2:
                #     print(f'Error Message1: \n{error_message2}')
                #     tweet_field_we = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')))
                #     tweet_field_we.send_keys(f'ISP-CompanyX promised a {download_promise}Mbps(downloads) and a {upload_promise}Mbps(uploads) but has only given a {self.down}Mbps(downloads) and a {self.up}Mbps(uploads) according to speedtest.net!!')



                time.sleep(2)
                tweet_btn_we = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')))
                tweet_btn_we.click()
            except Exception as error_message:
                print(f'Error Message2:\n{error_message}')
                time.sleep(2)
                begin_sign_in_we2 = self.driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[2]/main/div/div/div[1]/div[2]/div[4]/div[2]/span/span')
                begin_sign_in_we2.click()
                time.sleep(1)
                begin_sign_in_we = self.driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[2]/main/div/div/div[1]/div[2]/a/div/span/span')
                begin_sign_in_we.click()

                time.sleep(3)
                email_we = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, 'text')))
                email_we.send_keys(username)
                email_we.send_keys(Keys.ENTER)

                try:
                    time.sleep(4)
                    phone_we = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input')))
                    phone_we.send_keys(phone)
                    phone_we.send_keys(Keys.ENTER)
                except Exception:
                    pass

                time.sleep(3)
                pass_we = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, 'password')))
                pass_we.send_keys(password)
                pass_we.send_keys(Keys.ENTER)

                time.sleep(5)
                tweet_field_we = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')))
                tweet_field_we.send_keys(f'ISP-CompanyX promised a {download_promise}Mbps(downloads) and a {upload_promise}Mbps(uploads) but has only given a {self.down}Mbps(downloads) and a {self.up}Mbps(uploads) according to speedtest.net!!')

                time.sleep(2)
                tweet_btn_we = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')))
                tweet_btn_we.click()
        else:
            pass
            # self.driver.quit()
