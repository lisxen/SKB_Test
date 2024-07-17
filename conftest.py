import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as firefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru',
                     help="Language for browser")


@pytest.fixture(scope="function")
def browser(request):

    with allure.step("Подготовка запуска браузера"):

        browser_name = request.config.getoption("browser_name")
        language = request.config.getoption("language")

        browser = None

        if browser_name == "chrome":
            with allure.step("Запуск Chrome"):
                options = chromeOptions()
                options.add_experimental_option('prefs', {'intl.accept_languages': language})
                browser = webdriver.Chrome(options=options)

        elif browser_name == "firefox":
            with allure.step("Запуск Firefox"):
                options = firefoxOptions()
                options.set_preference('intl.accept_languages', language)
                browser = webdriver.Firefox()

        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")

        yield browser

    with allure.step("Завершение работы браузера"):
        browser.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
