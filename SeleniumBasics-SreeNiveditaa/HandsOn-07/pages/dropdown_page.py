from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class DropdownPage(BasePage):

    # Locator
    DROPDOWN = (By.ID, "select-demo")

    def __init__(self, driver):
        super().__init__(driver)

    def select_by_text(self, text):
        dropdown = Select(
            self.wait_for_element(self.DROPDOWN)
        )
        dropdown.select_by_visible_text(text)

    def select_by_value(self, value):
        dropdown = Select(
            self.wait_for_element(self.DROPDOWN)
        )
        dropdown.select_by_value(value)

    def select_by_index(self, index):
        dropdown = Select(
            self.wait_for_element(self.DROPDOWN)
        )
        dropdown.select_by_index(index)

    def get_selected_option(self):
        dropdown = Select(
            self.wait_for_element(self.DROPDOWN)
        )
        return dropdown.first_selected_option.text