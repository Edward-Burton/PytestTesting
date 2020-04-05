from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from testing.page.search import Search


class Main():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver,30)
        self.driver.get("https://home.testing-studio.com/")

    def search(self,keyword=None):
        self.driver.find_element(By.CSS_SELECTOR,"#search-button").click()
        searchinput = self.driver.find_element(By.CSS_SELECTOR,'[id="search-term"]')
        searchinput.send_keys("selenium")
        searchinput.send_keys(Keys.ENTER)
        return Search(self.driver)