from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def find_element(self, locator: tuple[str, str]):
        try:
            element = self.browser.find_element(*locator)
            return element
        except NoSuchElementException:
            raise NoSuchElementException

    def element_to_be_clickable(self, locator: tuple[str, str]):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator))
