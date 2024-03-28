import time

import pytest

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        self.go_to_login_page()
        self.should_be_registration_email_field()
        self.should_be_registration_email_field_send_keys(email)
        self.should_be_registration_password_1_field()
        self.should_be_registration_password_1_field_send_keys(password)
        self.should_be_registration_password_2_field()
        self.should_be_registration_password_2_field_send_keys(password)
        self.should_be_register_button()
        self.should_be_to_register_button_clickable()




    def should_be_register_button(self):
        assert self.is_element_present(*LoginPageLocators.BUTTON_TO_REGISTER), 'there is no to_register_button'


    def should_be_to_register_button_clickable(self):
        self.driver.find_element(*LoginPageLocators.BUTTON_TO_REGISTER).click()


    def should_be_logout_button(self):
        assert self.is_element_present(*LoginPageLocators.BUTTON_LOGOUT_ACCOUNT), 'there is no logout_button'


    def should_be_registration_email_field(self):
        assert self.is_element_present(*LoginPageLocators.FIELD_EMAIL)


    def should_be_registration_password_1_field(self):
        assert self.is_element_present(*LoginPageLocators.FIELD_PASSWORD_TO_CREATE_NEW1)


    def should_be_registration_password_2_field(self):
        assert self.is_element_present(*LoginPageLocators.FIELD_PASSWORD_TO_CREATE_NEW2)


    def should_be_registration_email_field_send_keys(self, email):
        self.driver.find_element(*LoginPageLocators.FIELD_EMAIL).send_keys(email)


    def should_be_registration_password_1_field_send_keys(self, password):
        self.driver.find_element(*LoginPageLocators.FIELD_PASSWORD_TO_CREATE_NEW1).send_keys(password)


    def should_be_registration_password_2_field_send_keys(self, password):
        self.driver.find_element(*LoginPageLocators.FIELD_PASSWORD_TO_CREATE_NEW2).send_keys(password)


    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.driver.current_url
        login = 'login'
        assert login in current_url, f'"{login}" is not in current url: {current_url}'


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        form_login = self.is_element_present(*LoginPageLocators.FORM_LOGIN)
        assert form_login, "Can't find form_login"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        form_registration = self.is_element_present(*LoginPageLocators.FORM_REGISTRATION)
        assert form_registration, "Can't find form_registration"