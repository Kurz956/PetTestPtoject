link = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(driver):
    login_link = driver.find_element('css selector', "#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(driver):
   driver.get(link)
   go_to_login_page(driver)