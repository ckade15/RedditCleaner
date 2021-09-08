from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

login_url = "https://www.reddit.com/login"
# chrome_options = Options()
# chrome_options.add_argument("--headless")

class Reddit:
    def __init__(self, user, password):
        self.driver = webdriver.Chrome()
        self.user = user
        self.password = password
        self.saved = f"https://www.reddit.com/user/{user}/saved"
    def login(self):
        self.login = self.driver.get(login_url)
        self.driver.find_element_by_id("loginUsername").send_keys(user)
        self.driver.find_element_by_id('loginPassword').send_keys(password)
        self.driver.find_element_by_css_selector("button[type='submit']").click()
    def rm_saved(self):
        self.driver.get(self.saved)
        section = 0
        while True:
            section += 1
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            print(f"One section of scrolling deleted. Sections deleted: {section}")
            self.driver.execute_script("for (let i = 1; i < document.getElementsByTagName('button').length; i++){if (document.getElementsByTagName('button')[i].innerText == 'unsave'){document.getElementsByTagName('button')[i].click()}}")
        


user = input("Enter your Reddit username: ")
password = input("Enter your Reddit password: ")

red = Reddit(user, password)
red.login()
time.sleep(3)
red.rm_saved()
