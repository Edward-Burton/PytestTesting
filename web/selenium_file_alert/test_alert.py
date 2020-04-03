from time import sleep

from selenium.webdriver import ActionChains

from web.selenium_window_frame.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #切换到frame下，获取两个元素执行拖拽操作
        self.driver.switch_to_frame("iframeResult")
        action = ActionChains(self.driver)
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        action.drag_and_drop(drag,drop)
        action.perform()

        print("点击alert 确认")
        self.driver.switch_to_alert().accept()
        self.driver.switch_to_default_content()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)

