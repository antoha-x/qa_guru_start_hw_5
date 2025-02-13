import os

from selene import browser, have


def test_fill_form_and_check_result_table():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Vasiliy')
    browser.element('#lastName').type('Pupkin')
    browser.element('#userEmail').type('tests@tests.ts')
    browser.element("[for='gender-radio-1']").click()
    browser.element('#userNumber').type('9876543210')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element("[value='0']").click()
    browser.element('.react-datepicker__year-select').click().element("[value='1990']").click()
    browser.element('.react-datepicker__day--001:not(.react-datepicker__day--outside-month)').click()

    browser.element('#subjectsInput').type('Maths')
    browser.element('#react-select-2-option-0').click()
    browser.element("[for='hobbies-checkbox-2']").click()
    browser.element('#uploadPicture').type(os.path.abspath('../resources/m527697.jpg'))
    browser.element('#currentAddress').type('Royal Road, Mont Choisy Mauritius, Mont Choisy, Mauritius Island')

    browser.element('#submit').hover()

    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()

    browser.element('#city').click()
    browser.element('#react-select-4-option-2').click()

    browser.element('#submit').click()

    browser.element(".modal-content").element("tbody").all("tr").all("td").even.should(have.exact_texts((
        'Vasiliy Pupkin',
        'tests@tests.ts',
        'Male',
        '9876543210',
        '01 January,1990',
        'Maths',
        'Reading',
        'm527697.jpg',
        'Royal Road, Mont Choisy Mauritius, Mont Choisy, Mauritius Island',
        'NCR Noida'
    )))
