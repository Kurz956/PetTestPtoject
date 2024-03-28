import pytest
from .locators import BasePageLocators, BasketPageLocators
from .base_page import BasePage



class BasketPage(BasePage):
    def should_be_visible_button_card(self):
        assert self.is_element_present(*BasePageLocators.BUTTON_CARD), 'Button_card is not visible'


    def should_go_to_card(self):
        button_card = self.driver.find_element(*BasePageLocators.BUTTON_CARD)
        button_card.click()


    def should_be_empty_card(self):
        assert self.is_not_element_present(*BasketPageLocators.CARD), 'Card is not empty'


    def should_be_message_empty_card(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY), 'No message that "card is not empty"'
