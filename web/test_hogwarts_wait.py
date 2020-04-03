import time

from selenium import webdriver #导入依赖模块
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts():
    def setup(self): #初始化
        # self.driver = webdriver.Firefox(executable_path="")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        #隐式等待：加载下一个页面最长等5秒，等到就执行，等5秒没等到就抛异常
        #加载过程中，隐式等待只能查找到DOM数，找到你点击的元素，不能知道这个元素是否可点击，是否可见，
    def teardown(self):
        self.driver.quit() #回收driver，页面退出关闭
    def test_hogwarts(self):
        self.driver.get("https://testerhome.com")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("霍格沃兹测试学院").click()
        self.driver.find_element_by_css_selector(".topic-22832 .title > a").click()
    def test_timewait(self):
        self.driver.get("https://testerhome.com")
        self.driver.find_element(By.XPATH,'//*[@title="2020年 第一季度招聘贴"]').click()
        self.driver.find_element(By.XPATH,'//*[@href="/github_statistics"]').click()
        def test_wait(d):
            return self.driver.find_element(By.XPATH, '//*[@class="panel-heading"]')
        #显示等待
        #WebDriverWait(self.driver,10).until(test_wait) #传参为函数，参数不写括号
        # 可直接调用该函数expected_conditions
        WebDriverWait(self.driver, 10).until(expected_conditions.
        element_to_be_clickable(By.XPATH,'//*[@href="/topics/last"]'))  # 传参为函数，参数不写括号

    def test_locator(self):
        self.driver.get("https://cn.bing.com/")
        self.driver.find_element(By.XPATH,'//*[@id="sb_form_q"]').send_keys("离开")
        self.driver.find_element(By.CSS_SELECTOR,'[id=sb_form_go]').click()
