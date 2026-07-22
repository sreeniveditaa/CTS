from pages.input_form_page import InputFormPage


def test_input_form(driver):

    page = InputFormPage(driver)

    page.navigate_to(
        "https://www.lambdatest.com/selenium-playground/input-form-demo"
    )

    page.enter_name("Sree")

    page.enter_email("sree@gmail.com")

    page.enter_password("Test123")

    page.enter_company("CTS")

    page.enter_website("www.cts.com")

    page.select_country("India")

    page.enter_city("Chennai")

    page.enter_address1("Anna Nagar")

    page.enter_address2("Near Metro")

    page.enter_state("Tamil Nadu")

    page.enter_zip("600001")

    page.click_submit()