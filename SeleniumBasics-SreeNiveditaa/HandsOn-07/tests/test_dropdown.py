from pages.dropdown_page import DropdownPage


def test_dropdown(driver):

    page = DropdownPage(driver)

    page.navigate_to(
        "https://www.lambdatest.com/selenium-playground/select-dropdown-demo"
    )

    page.select_by_text("Monday")

    assert page.get_selected_option() == "Monday"