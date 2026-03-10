import pytest
from selene import browser, by, be, have, command
from pathlib import Path

def test_fill_and_submit_form():
    # Создаём временный файл для загрузки (абсолютный путь)
    file_name = 'test.png'
    file_path = str(Path(file_name).resolve())
    with open(file_path, 'wb') as f:
        f.write(b'')

    try:
        # Открыть страницу с формой
        browser.open('/automation-practice-form')

        # Заполнить имя
        browser.element('#firstName').type('Leonid')
        # Заполнить фамилию
        browser.element('#lastName').type('Gromov')
        # Заполнить email
        browser.element('#userEmail').type('test@qaguru.ru')
        # Выбрать пол (Male)
        browser.element('[for="gender-radio-1"]').click()
        # Номер телефона (10 цифр)
        browser.element('#userNumber').type('1234567890')

        # Дата рождения (28 августа 2004)
        # Упрощённый вариант: прямой ввод (работает на demoqa.com)
        browser.element('#dateOfBirthInput').type('28 Aug 2004').press_enter()
        # Альтернатива через селекты (если нужен клик):
        # browser.element('#dateOfBirthInput').click()
        # browser.element('.react-datepicker__year-select').click()
        # browser.element('[value="2004"]').click()
        # browser.element('.react-datepicker__month-select').click()
        # browser.element('[value="7"]').click()  # август = 7 (январь = 0)
        # browser.element('.react-datepicker__day--028').click()

        # Выбрать хобби (Sports и Reading)
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('[for="hobbies-checkbox-2"]').click()

        # Заполнить текущий адрес
        browser.element('#currentAddress').type('88 Colin P. Kelly Jr. Street.San Francisco')

        # Загрузка файла
        browser.element('#uploadPicture').type(file_path)  # используем абсолютный путь

        # Выбрать штат (Rajasthan)
        browser.element('#state').click()
        browser.element(by.text('Rajasthan')).click()

        # Выбрать город (Jaipur)
        browser.element('#city').click()
        browser.element(by.text('Jaipur')).click()

        # Отправить форму (JS-клик из-за возможной рекламы)
        browser.element('#submit').perform(command.js.click)

        # Проверить появление модального окна
        browser.element('.modal-content').should(be.visible)
        browser.element('#example-modal-sizes-title-lg').should(
            have.text('Thanks for submitting the form')
        )

        # Проверить данные в таблице модального окна
        # Порядок полей: Student Name, Email, Gender, Mobile, Date of Birth, Subjects, Hobbies, Picture, Address, State and City
        browser.element('.table').all('td').even.should(have.exact_texts(
            'Leonid Gromov',
            'test@qaguru.ru',
            'Male',
            '1234567890',
            '28 August,2004',          # формат точно такой, как на странице
            '',                          # Subjects (мы не заполняли)
            'Sports, Reading',
            'test.png',
            '88 Colin P. Kelly Jr. Street.San Francisco',
            'Rajasthan Jaipur'
        ))

    finally:
        # Удаляем временный файл
        Path(file_path).unlink(missing_ok=True)