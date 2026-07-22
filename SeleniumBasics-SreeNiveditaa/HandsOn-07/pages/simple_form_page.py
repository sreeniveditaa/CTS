from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.base_page import BasePage


class SimpleFormPage(BasePage):

    MESSAGE_INPUT = (By.ID, "user-message")
    SUBMIT_BUTTON = (By.ID, "showInput")
    DISPLAY_MESSAGE = (By.ID, "message")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_message(self, text):
        self.wait_for_element(self.MESSAGE_INPUT).send_keys(text)

    def click_submit(self):
        time.sleep(5)
        button = self.wait_until_clickable(
            self.SUBMIT_BUTTON
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    def get_displayed_message(self):

        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                self.DISPLAY_MESSAGE,
                "Hello Selenium"
            )
        )

        return self.driver.find_element(*self.DISPLAY_MESSAGE).text