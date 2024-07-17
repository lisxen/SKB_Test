import allure
from datetime import datetime, timedelta

import pytest

from pages.cell_list_page import CellListPage


class TestCellList:

    link = "https://samples.gwtproject.org/samples/Showcase/Showcase.html#!CwCellList"

    @allure.title("Обновление данных контакта")
    @allure.description("Внесение изменений в текстовые поля первого контакта в списке")
    @pytest.mark.positive
    def test_update_contact_info(self, browser):
        first_name = "John"
        second_name = "Snow"
        address = "Winterfell"

        page = CellListPage(browser, self.link)
        page.choose_first_contact()
        page.send_first_name(first_name)
        page.send_second_name(second_name)
        page.send_address(address)
        page.click_on_update_contact_button()
        page.should_be_contact_in_list(first_name, second_name, address)

    @allure.title("Создание нового контакта")
    @allure.description("Создание нового контакта с заданными данными")
    @pytest.mark.positive
    def test_create_contact(self, browser):
        first_name = "John"
        second_name = "Snow"
        address = "Winterfell"
        b_day = "Mar 15, 2013"

        page = CellListPage(browser, self.link)
        page.send_first_name(first_name)
        page.send_second_name(second_name)
        page.send_birthday_date(b_day)
        page.send_address(address)
        page.click_on_create_contact_button()
        page.should_be_created()

    @allure.title("Замена данных контакта на пустые значения")
    @allure.description("Замена заполняемых информационных полей в карточке контакта на пустые значения")
    @pytest.mark.negative
    def test_update_contact_with_empty_inputs(self, browser):
        first_name = ""
        second_name = ""
        address = ""
        b_day = ""

        page = CellListPage(browser, self.link)
        page.choose_first_contact()
        page.send_first_name(first_name)
        page.send_second_name(second_name)
        page.send_birthday_date(b_day)
        page.send_address(address)
        page.click_on_update_contact_button()
        page.should_be_not_updated()

    @allure.title("Создание контакта с датой рождения больше текущей")
    @allure.description("Создание контакта с датой рождения больше текущей на 1 день")
    @pytest.mark.negative               
    def test_create_contact_with_future_bday_date(self, browser):
        first_name = "John"
        second_name = "Snow"
        address = "Winterfell"
        b_day = (datetime.now() + timedelta(days=1)).strftime("%B %d, %Y")

        page = CellListPage(browser, self.link)
        page.send_first_name(first_name)
        page.send_second_name(second_name)
        page.send_birthday_date(b_day)
        page.send_address(address)
        page.click_on_create_contact_button()
        page.should_be_not_created()
