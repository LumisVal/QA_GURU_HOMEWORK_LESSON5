import pytest
from selene import browser, by, be, have, command


def test_fill_and_submit_form():
    # Открыть страницу с формой
    browser.open('/automation-practice-form')

    # Заполнить имя
    browser.element('#firstName').type('Leonid')
    # Заполнить фамилию
    browser.element('#lastName').type('Gromov')
    # Заполнить email
    browser.element('#userEmail').type('test@qaguru.ru')
    # Выбрать пол (например, Male)
    browser.element('[for="gender-radio-1"]').click()
    # Добавим номер телефона
    browser.element('#userNumber').type('123456789')
    #Добавим дату рождения через иммитацию кликов
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="2004"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="8"]').click()
    browser.element('.react-datepicker__day--028').click()

    # Выбрать предмет (например, Maths)
    browser.element('#subjectsInput').type('Maths').press_enter()

    # Выбрать хобби (Sports и Reading)
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()

    # Заполнить текущий адрес
    browser.element('#currentAddress').type('88 Colin P. Kelly Jr. Street.San Francisco')

    # Выбрать штат (например, Rajasthan)
    browser.element('#state').click()
    browser.element(by.text('Rajasthan')).click()

    # Выбрать город (например, Jaipur)
    browser.element('#city').click()
    browser.element(by.text('Jaipur')).click()

    # Отправить форму (иногда требуется JS-клик из-за перекрывающей рекламы)
    browser.element('#submit').perform(command.js.click)

    # Проверить, что появилось модальное окно с подтверждением
    browser.element('.modal-content').should(be.visible)
    browser.element('#example-modal-sizes-title-lg').should(
        have.text('Thanks for submitting the form')
    )