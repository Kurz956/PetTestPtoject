from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.driver.current_url
        assert 'login' in current_url, f'"login" is not in current url: {current_url}'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        form_login = self.is_element_present(*LoginPageLocators.FORM_LOGIN)
        assert False, "Can't find form_login"   # поменять на form_login

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        form_registration = self.is_element_present(*LoginPageLocators.FORM_REGISTRATION)
        assert False, "Can't find form_registration"  # поменять на form_registration