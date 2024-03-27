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
        for offer_number in range(10)]


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(driver, link):
    print(link)
    page = ProductPage(driver, link)
    page.open()
    page.should_be_add_to_card_stuff()
    page.should_add_to_card_stuff()
    page.solve_quiz_and_get_code()
    page.should_be_successful_added_massage()
    page.should_be_successful_card_massage()
    page.should_same_shop_item_name_with_added_item()
    page.should_be_correct_price_massage()
    page.should_be_correct_price()
    time.sleep(3)






