from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.driver.find_element('css selector', "#login_link")
        login_link.click()
