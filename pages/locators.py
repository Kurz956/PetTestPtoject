
class BasePageLocators():
    LOGIN_LINK = ('css selector', "#login_link")
    LOGIN_LINK_INVALID = ('css selector', "#login_link_inc")
    BUTTON_CARD = ('css selector', 'span.btn-group > a')
    USER_ICON = ('css selector', ".icon-user")

class BasketPageLocators():
    MESSAGE_EMPTY = ('css selector', '#content_inner > p')
    CARD = ('css selector', '.basket_summary')
class MainPageLocators():
    LOGIN_LINK = ('css selector', "#login_link")

class LoginPageLocators():
    FORM_LOGIN = ('css selector', "#login_form")
    FORM_REGISTRATION = ('css selector', "#register_form")
    FIELD_EMAIL = ('css selector', 'input[name="registration-email"]')
    FIELD_PASSWORD_TO_CREATE_NEW1 = ('css selector', 'input[name="registration-password1"]')
    FIELD_PASSWORD_TO_CREATE_NEW2 = ('css selector', 'input[name="registration-password2"]')
    BUTTON_TO_REGISTER = ('css selector', 'button[name="registration_submit"]')
    BUTTON_LOGOUT_ACCOUNT = ('css selector', '#logout_link')


class ProductPageLocators():
    BUTTON_ADD_TO_CARD = ('css selector', '.btn.btn-lg.btn-primary.btn-add-to-basket')
    ITEM_NAME = ('css selector', '.col-sm-6.product_main > h1')
    ITEM_ADDED_TO_CARD_SUCCESS = ('xpath', "(//div[@class='alertinner '])[1]//strong")
    FIELD_YOUR_CARD_SUCCESS = ('xpath', "(//div[@class='alertinner '])[2]")
    PRICE_OF_THE_CARD = ('xpath', "(//div[@class='alertinner '])[3]//strong")
    PRICE_OF_THE_ITEM = ('css selector', '.col-sm-6.product_main>p.price_color')

