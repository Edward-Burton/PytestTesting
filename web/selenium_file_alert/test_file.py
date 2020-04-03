from time import sleep

from web.selenium_window_frame.base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id('stfile').send_keys('C:\\Users\\Lin\\Pictures\\him.jpg')
        sleep(3)
