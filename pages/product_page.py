from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_item_to_card_button(self):
        '''add_item_to_card_button is on the page'''
        add_item_to_card_button = self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CARD)
        assert add_item_to_card_button, "Can't find button_add_to_card"

    def should_add_item_to_card(self):
        '''adding item o the cart'''
        add_item_to_card = self.driver.find_element(*ProductPageLocators.BUTTON_ADD_TO_CARD)
        add_item_to_card.click()


    def should_be_successful_added_message(self):
        '''should be message "has been successfully added to the cart"'''
        successful_added_message = self.is_element_present(*ProductPageLocators.ITEM_ADDED_TO_CARD_SUCCESS)
        assert successful_added_message, "Can't find successful_added_message"
        name_of_the_added_item = self.driver.find_element(*ProductPageLocators.ITEM_ADDED_TO_CARD_SUCCESS).text
        print(f'Item "{name_of_the_added_item}" has been successfully added to the cart')

    def should_be_successful_card_message(self):
        '''should be message "cart is Deferred benefit offer"'''
        successful_card_message = self.is_element_present(*ProductPageLocators.FIELD_YOUR_CARD_SUCCESS)
        assert successful_card_message, "Can't find successful_card_message"

    def should_same_shop_item_name_with_added_item(self):
        '''name of the added item in cart is equal with name from the shop'''
        shop_item_name = self.driver.find_element(*ProductPageLocators.ITEM_NAME).text
        name_of_the_added_item = self.driver.find_element(*ProductPageLocators.ITEM_ADDED_TO_CARD_SUCCESS).text
        assert shop_item_name == name_of_the_added_item, f"Names of the items are different" \
                                                         f" '{name_of_the_added_item}' != '{shop_item_name}'"

    def should_be_correct_price_massage(self):
        '''check that the item price is correct '''
        correct_price_message = self.is_element_present(*ProductPageLocators.PRICE_OF_THE_CARD)
        assert correct_price_message, "Can't find correct_price_message"


    def should_be_correct_price(self):
        '''cart price should be equal with item price in single adding'''
        price_item = self.driver.find_element(*ProductPageLocators.PRICE_OF_THE_ITEM).text
        price_card = self.driver.find_element(*ProductPageLocators.PRICE_OF_THE_CARD).text
        assert price_item == price_card, f'price should be {price_item}, yours is {price_card}'
        print(f'final price is {price_card}')

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_ADDED_TO_CARD_SUCCESS), \
            "Success message is presented, but should not be"


    def should_success_message_disappear(self):
        success_message = self.is_disappeared(*ProductPageLocators.ITEM_ADDED_TO_CARD_SUCCESS)
        assert success_message, 'Success message adding item to card not disappeared'