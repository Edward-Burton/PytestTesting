import time

import pytest

from web.selenium_window_frame.base import Base


class TestJS(Base):

    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("http:www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        #获得JS返回必须加return
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        time.sleep(3)
        #执行滚动操作
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        self.driver.find_element_by_xpath("//*[@id='page']/a[10]").click()
        time.sleep(3)

        #返回页面信息
        # for code in[
        #     'return document.title',"return JSON.stringify(performance.timing)"
        # ]:
        #     print(self.driver.execute_script(code))
        print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))

    def test_js_time(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("a = document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script('document.getElementById("train_date").value="2020-12-24"')
        time.sleep(3)