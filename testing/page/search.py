from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver


class Search:
    def __init__(self,driver):
        self.driver:WebDriver= driver

    def search_by(self,author=None,keyword=None):
        if keyword is not None:
            input = self.driver.find_element(By.CSS_SELECTOR,'input.search-query')
            input.clear()
            input.send_keys(keyword)
            #input.send_keys(Keys.ENTER)
        if author is not None:
            self.driver.find_element(By.CSS_SELECTOR, '[name="user-selector-renamed"]').send_keys(author)
            self.driver.find_element(By.CSS_SELECTOR, 'li .selected').click()
            # self.driver.find_element(By.CSS_SELECTOR,'button .search-cta').click()
        self.driver.find_element(By.CSS_SELECTOR,'.search-bar button').click()
        return self

    def get_results(self):
        #获取结果列表，element.text包括作者和内容
        return [element.text for element in self.driver.find_elements(By.CSS_SELECTOR,'.fps-result')]

    def get_author(self):
        return [element.get_attribute("data-user-card") for element in self.driver.find_elements(By.CSS_SELECTOR,'.fps-result .author a')]
