# Тестовое задание для QA-инженера

## Задание 
Необходимо составить и реализовать не менее 4 тест-кейсов 
для проведения автоматизированного тестирования с использованием 
Selenium WebDriver, Allure (необходимо создавать скриншот 
у проваленных тестов), для списка контактов.

## Используемые библиотеки
- **PyTest** - основной фреймворк для автоматизации тестирования
- **Selenium** - инструмент для автоматизации тестирования веб-приложения
- **Allure** - для генерации отчетов по тестированию
- **BeautifulSoup** - для парсинга веб-страницы
- **PyTest-xdist** - для распараллеливания выполнения автотестов

## Команды для запуска
`pytest --alluredir=allure_results -n=2` - запуск тестов в 2 потоках с генерацией отчета
в папку allure_results

`allure serve allure_results` - генерация и запуск временного веб-сервера
для просмотра отчета по пройденным автотестам
