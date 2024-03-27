from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_add_to_card_item_button(self):
        # button_add_to_card присутствует на странице
        button_add_to_card = self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CARD)
        assert button_add_to_card, "Can't find button_add_to_card"

    def should_add_item_to_card(self):
        # button_add_to_card кликабельна
        button_add_to_card = self.driver.find_element(*ProductPageLocators.BUTTON_ADD_TO_CARD)
        button_add_to_card.click()


    def should_be_successful_added_massage(self):
        # сообщение "был добавлен в вашу корзину."
        successful_added_massage = self.is_element_present(*ProductPageLocators.ITEM_ADDED_TO_CARD_SUCCESS)
        assert successful_added_massage, "Can't find successful_added_massage"
        name_of_the_added_item = self.driver.find_element(*ProductPageLocators.ITEM_ADDED_TO_CARD_SUCCESS).text
        print(f'Item "{name_of_the_added_item}" has been successfully added to the cart')

    def should_be_successful_card_massage(self):
        # сообщение "Ваша корзина удовлетворяет условиям предложения Deferred benefit offer"
        successful_card_massage = self.is_element_present(*ProductPageLocators.FIELD_YOUR_CARD_SUCCESS)
        assert successful_card_massage, "Can't find successful_card_massage"

    def should_same_shop_item_name_with_added_item(self):
        # имя добавленного товара совпадает с именем товара из магазина
        shop_item_name = self.driver.find_element(*ProductPageLocators.ITEM_NAME).text
        name_of_the_added_item = self.driver.find_element(*ProductPageLocators.ITEM_ADDED_TO_CARD_SUCCESS).text
        assert shop_item_name == name_of_the_added_item, f"names of the items are different" \
                                                         f" '{name_of_the_added_item}' != '{shop_item_name}'"

    def should_be_correct_price_massage(self):
        # проверка корректности цены товара и корзины
        correct_price_massage = self.is_element_present(*ProductPageLocators.PRICE_OF_THE_CARD)
        assert correct_price_massage, "Can't find correct_price_massage"

    def should_be_correct_price(self):
        # сообщение "Стоимость корзины теперь составляет {....} £"
        price_item = self.driver.find_element(*ProductPageLocators.PRICE_OF_THE_ITEM).text
        price_card = self.driver.find_element(*ProductPageLocators.PRICE_OF_THE_CARD).text
        assert price_item == price_card, f'price should be {price_item}, yours is {price_card}'
        print(f'final price is {price_card}')

    def should_not_be_success_message(self):
        # при открытии страницы товара он не должен быть сразу добавлен в корзину
        success_massage = self.is_not_element_present(*ProductPageLocators.ITEM_ADDED_TO_CARD_SUCCESS)
        assert success_massage, 'success_massage arise before adding item to card'

    def should_success_message_disappear(self):
        # сообщение об успешном добавлении должна исчезнуть через некоторое время после появления
        success_massage = self.is_disappeared(*ProductPageLocators.ITEM_ADDED_TO_CARD_SUCCESS)
        assert success_massage, 'success_massage adding item to card not disappeared'