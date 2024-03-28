from pages.base_page import BasePage
from pages.locators import BasePageLocators, BasketPageLocators


class BasketPage(BasePage):
    def should_be_visible_button_card(self):
        assert self.is_element_present(*BasePageLocators.BUTTON_CARD), 'button_card not visible'


    def should_go_to_card(self):
        button_card = self.driver.find_element(*BasePageLocators.BUTTON_CARD)
        button_card.click()


    def should_be_empty_card(self):
        assert self.is_not_element_present(*BasketPageLocators.CARD), 'card is not empty'


    def should_be_message_empty_card(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY), 'no message that "card is not empty"'
