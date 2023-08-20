from selene import browser, be, have


def test_practice_form(setup_browser):
    # the values we're testing
    name = "test_name"
    last_name = "test_last_name"
    email = "test@gmail.com"
    gender = "Female"
    number = "0123456789"
    date_of_birth = "01 January,1942"
    subject_0 = "History"
    subject_1 = "Maths"
    hobbies = "Reading, Music"
    address = "Some-street, Some-house, Some-apartment"
    state = "Haryana"
    city = "Panipat"

    browser.open("/automation-practice-form")

    # fill in the basic stuff
    browser.element("#firstName").type(name)
    browser.element("#lastName").type(last_name)
    browser.element("#userEmail").type(email)
    browser.element('[for="gender-radio-2"]').click()
    browser.element("#userNumber").type(number)

    # fill in the date
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click()
    browser.element(".react-datepicker__month-select [value='0']").click()
    browser.element(".react-datepicker__year-select").click()
    browser.element(".react-datepicker__year-select [value='1942']").click()
    browser.element(".react-datepicker__day.react-datepicker__day--001").click()

    # fill in the hobbies
    browser.element("#subjectsInput").type(subject_0).press_enter()
    browser.element("#subjectsInput").type(subject_1).press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    # fill in the full address
    browser.element("#currentAddress").type(address)
    browser.element("#react-select-3-input").type(state).press_enter()
    browser.element("#react-select-4-input").type(city).press_enter()

    browser.element("#submit").press_enter()

    # now, check it all
    browser.element(".table").should(have.text(name))
    browser.element(".table").should(have.text(last_name))
    browser.element(".table").should(have.text(email))
    browser.element(".table").should(have.text(gender))
    browser.element(".table").should(have.text(number))
    browser.element(".table").should(have.text(date_of_birth))
    browser.element(".table").should(have.text(subject_0))
    browser.element(".table").should(have.text(subject_1))
    browser.element(".table").should(have.text(hobbies))
    browser.element(".table").should(have.text(address))
    browser.element(".table").should(have.text(state))
    browser.element(".table").should(have.text(city))
