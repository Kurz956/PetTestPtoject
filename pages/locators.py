
class BasePageLocators():
    LOGIN_LINK = ('css selector', "#login_link")
    LOGIN_LINK_INVALID = ('css selector', "#login_link_inc")
class MainPageLocators():
    LOGIN_LINK = ('css selector', "#login_link")

class LoginPageLocators():
    FORM_LOGIN = ('css selector', "#login_form")
    FORM_REGISTRATION = ('css selector', "#register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_CARD = ('css selector', '.btn.btn-lg.btn-primary.btn-add-to-basket')
    ITEM_NAME = ('css selector', '.col-sm-6.product_main > h1')
    ITEM_ADDED_TO_CARD_SUCCESS = ('xpath', "(//div[@class='alertinner '])[1]//strong")
    FIELD_YOUR_CARD_SUCCESS = ('xpath', "(//div[@class='alertinner '])[2]")
    PRICE_OF_THE_CARD = ('xpath', "(//div[@class='alertinner '])[3]//strong")
    PRICE_OF_THE_ITEM = ('css selector', '.col-sm-6.product_main>p.price_color')

