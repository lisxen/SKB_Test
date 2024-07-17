import allure
from pages.base_page import BasePage
from  bs4 import BeautifulSoup
from locators.cell_list_locators import CellListLocators
from selenium.webdriver.common.keys import Keys


class CellListPage(BasePage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.browser.get(self.url)

    @allure.step("Выбор первого контакта в листе")
    def choose_first_contact(self):
        first_contact = self.element_to_be_clickable(CellListLocators.FIRST_CONTACT)
        first_contact.click()

    @allure.step("Нажатие кнопки Обновить")
    def click_on_update_contact_button(self):
        update_btn = self.element_to_be_clickable(CellListLocators.UPDATE_BUTTON)
        update_btn.click()

    @allure.step("Нажатие кнопки Создать")
    def click_on_create_contact_button(self):
        create_btn = self.element_to_be_clickable(CellListLocators.CREATE_BUTTON)
        create_btn.click()

    @allure.step("Ввод имени")
    def send_first_name(self, exp_first_name: str):
        first_name_input = self.find_element(CellListLocators.FIRST_NAME_INPUT)
        first_name_input.clear()
        first_name_input.send_keys(exp_first_name)

    @allure.step("Ввод фамилии")
    def send_second_name(self, exp_second_name: str):
        second_name_input = self.find_element(CellListLocators.SECOND_NAME_INPUT)
        second_name_input.clear()
        second_name_input.send_keys(exp_second_name)

    @allure.step("Ввод даты рождения")
    def send_birthday_date(self, exp_b_day: str):
        b_day_input = self.find_element(CellListLocators.BIRTHDAY_INPUT)
        b_day_input.clear()
        b_day_input.send_keys(exp_b_day)
        b_day_input.send_keys(Keys.ENTER)

    @allure.step("Ввод адреса")
    def send_address(self, exp_address: str):
        address_input = self.find_element(CellListLocators.ADDRESS_INPUT)
        address_input.clear()
        address_input.send_keys(exp_address)

    @allure.step("Проверка наличия контакта в листе с указанными Фамилия+Имя+Адрес")
    def should_be_contact_in_list(self, first_name: str, second_name: str, address: str):
        full_name = first_name + " " + second_name
        first_contact = self.find_element(CellListLocators.FIRST_CONTACT)
        first_contact_html = first_contact.get_attribute("innerHTML")
        soup = BeautifulSoup(first_contact_html, "html.parser")
        contact_info = soup.find_all("td")[1:]
        assert contact_info[0].get_text() == full_name
        assert contact_info[1].get_text() == address

    @allure.step("Проверка создания нового контакта через счетчик")
    def should_be_created(self):
        contact_counter = self.find_element(CellListLocators.CONTACT_COUNTER)
        count = int(contact_counter.text.split(":")[1].strip())
        assert count == 251, "Контакт не был создан!"

    @allure.step("Проверка отсутствия обновления на пустые поля")
    def should_be_not_updated(self):
        first_contact = self.find_element(CellListLocators.FIRST_CONTACT)
        first_contact_html = first_contact.get_attribute("innerHTML")
        soup = BeautifulSoup(first_contact_html, "html.parser")
        contact_info = soup.find_all("td")[1:]
        assert contact_info[0].get_text() == "", "Контакт обновлен пустыми значениями!"
        assert contact_info[1].get_text() == "", "Контакт обновлен пустыми значениями!"

    @allure.step("Проверка отсутствия создания нового контакта через счетчик")
    def should_be_not_created(self):
        contact_counter = self.find_element(CellListLocators.CONTACT_COUNTER)
        count = int(contact_counter.text.split(":")[1].strip())
        assert count == 250, "Контакт был создан!"
