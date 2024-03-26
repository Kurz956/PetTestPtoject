from .pages.main_page import MainPage
from .pages.login_page import LoginPage




def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    link_login = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = MainPage(driver, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


