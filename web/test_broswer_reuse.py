import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBrowserReuse:
    def setup_method(self, method):
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.debugger_address = "localhost:8083"
        # 调试模式下已登录
        self.driver = webdriver.Chrome(options=chrome_opts)
        self.driver.get("https://work.weixin.qq.com/")
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_weixin(self):
        # 获取复用浏览器的cookies
        cookies = self.driver.get_cookies()
        # 写入到文件
        with open("work_weixin_cookies", "w")as f:
            json.dump(cookies, f)
        # 读出到列表
        with open("work_weixin_cookies", "r")as f:
            cookies: list[tuple] = json.load(f)
            print(cookies)
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        # 获取访问后台管理首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 点击添加成员
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_item_title').click()
        # 点击添加头像
        self.driver.find_element(By.CSS_SELECTOR, '[class="member_edit_cover_avatar"]').click()
        self.driver.find_element(By.XPATH, '//*[@class="ww_fileInput js_file"]').send_keys(
            'C:\\Users\\Lin\\Pictures\\him.jpg')
        # 点击保存图片
        self.driver.find_element(By.CSS_SELECTOR, '[class="qui_btn ww_btn ww_btn_Blue js_save"]').click()
        # 添加姓名
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys("丁海寅")
        self.driver.find_element(By.CSS_SELECTOR, '[name=english_name]').send_keys("him")
        self.driver.find_element(By.CSS_SELECTOR, '[name=acctid]').send_keys('DingHaiYin')
        # 单选按钮点击
        self.driver.find_element(By.CSS_SELECTOR, '[value="1"]').click()
        self.driver.find_element(By.ID, "memberAdd_mail").send_keys("DingHaiYin@qq.com")
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_title').send_keys("男朋友")
        # 点击保存
        self.driver.find_element(By.XPATH, '//*[@class="qui_btn ww_btn js_btn_save"]').click()
        sleep(5)
