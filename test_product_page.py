import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import time

failed_tests = [7,]
product_link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
urls = [f'{product_link}{offer_number}' if offer_number not in failed_tests else
        pytest.param(
            f'{product_link}{offer_number}',
            marks=pytest.mark.xfail(reason='bug', strict=True)
        )
        for offer_number in range(1)] # range 10


@pytest.mark.skip
#@pytest.mark.xfail(reason='failing next step to adding item to card')
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    page = ProductPage(driver, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    page.open()
    page.should_be_add_to_card_item_button()
    page.should_add_item_to_card()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(driver):
    page = ProductPage(driver, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    page.open()
    page.should_not_be_success_message()




@pytest.mark.skip
#@pytest.mark.xfail(reason='success adding massage dont disappera')
def test_message_disappeared_after_adding_product_to_basket(driver):
    page = ProductPage(driver, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    page.open()
    page.should_add_item_to_card()
    page.should_success_message_disappear()


def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.skip
# @pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(driver, link):
    print(link)
    page = ProductPage(driver, link)
    page.open()
    page.should_not_be_success_message()
    page.should_be_add_to_card_item_button()
    page.should_add_item_to_card()
    page.solve_quiz_and_get_code()
    page.should_be_successful_added_massage()
    page.should_be_successful_card_massage()
    page.should_same_shop_item_name_with_added_item()
    page.should_be_correct_price_massage()
    page.should_be_correct_price()
    page.should_success_message_disappear()





