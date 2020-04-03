import time

import allure
import pytest
from selenium import webdriver

@allure.testcase("http://www.github.com")#链接到一个测试用例管理地址
@allure.feature("百度搜索")
@pytest.mark.parametrize('testdata',['allure','selenium','pytest'])
def test_steps_demo(testdata):

    with allure.step("打开百度网页"):
        driver=webdriver.Chrome("")
        driver.get("http://www.baidu.com")
        driver.maximize_window()


    with allure.step(f"输入关键字：{testdata}"):
        driver.find_element_by_id('kw').send_keys(testdata)
        time.sleep(2)
        driver.find_element_by_id('su').click()
        time.sleep(2)
    with allure.step("保存图片"):
        driver.save_screenshot("./result/b.png")
        allure.attach.file("./result/b.png",attachment_type=allure.attachment_type.PNG)

    with allure.step("退出浏览器"):
        driver.quit()