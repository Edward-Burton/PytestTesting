from appium.webdriver import webdriver

from testing import BasePage


class  App(BasePage):
    def start(self):
        _package="com.xueqiu.android"
        _activity=".view.WelcomActivityAlias"
        if self._driver is None:
            caps={}
            caps["platformName"]="android"
            caps["deviceName"]="hogwarts"
            caps["appPackage"]=_package
            caps["appActivity"]=_activity
            caps["autoGrantPermissions"]=True
            self._driver=webdriver.Remote("Http")