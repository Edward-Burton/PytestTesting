from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():

    #类变量
    _base_url = ""

    def __init__(self,driver:WebDriver=None):
        self._driver=""
        #防止每次调用都初始化新的driver，在调用第一个类时就进行创建
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self,by,locator):
        return self._driver.find_element(by,locator)