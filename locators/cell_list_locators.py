from selenium.webdriver.common.by import By


class CellListLocators:

    FIRST_CONTACT = (By.XPATH, "//div[@tabindex='-1']/div/div/div/div[1][not(@aria-hidden)]")

    FIRST_NAME_INPUT = (By.XPATH, "//td[text()=' First Name: ']/../td/input")
    SECOND_NAME_INPUT = (By.XPATH, "//td[text()=' Last Name: ']/../td/input")
    BIRTHDAY_INPUT = (By.XPATH, "//td[text()=' Birthday: ']/../td/input")
    ADDRESS_INPUT = (By.XPATH, "//td[text()=' Address: ']/../td/textarea")

    UPDATE_BUTTON = (By.XPATH, "//button[text() = 'Update Contact']")
    CREATE_BUTTON = (By.XPATH, "//button[text() = 'Create Contact']")

    CONTACT_COUNTER = (By.XPATH, "//div[@tabindex='-1']/../div[2]")
