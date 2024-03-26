import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: ru, en, fr, etc.. default is en')

@pytest.fixture(scope='function')
def driver(request):
    user_language = request.config.getoption('language')

    options = Options()
    options.add_experimental_option(
        'prefs',
        {'intl.accept_language': user_language}
    )

    driver = webdriver.Chrome(options=options)

    print('\nstart testing with chrome')
    yield driver
    print('\nquit browser')
    driver.quit()