from selenium.webdriver.common.by import By

from web.PO.page.basepage import BasePage


class Contact(BasePage):
    def get_Contacts(self):
        return [member.test for member in self.find(By.CSS_SELECTOR, 'tbody [data-type="member"]')]

    def get_top_contact(self, property=None):
        if property == None:
            return self.find(By.CSS_SELECTOR, '#member_list tr:nth-child(1)').text
        elif property == "name":
            #return self.find(By.CSS_SELECTOR, '#member_list tr:nth-child(1) td:nth-child(2)').get_attribute("title")
            return self._driver.find_element_by_css_selector('#member_list tr:nth-child(1) td:nth-child(2)').get_attribute("title")
        elif property == 'client':
            return self.find(By.CSS_SELECTOR, '#member_list tr:nth-child(1) td:nth-child(3)').get_attribute("title")
