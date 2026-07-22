from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InputFormPage(BasePage):

    NAME = (By.NAME, "name")
    EMAIL = (By.ID, "inputEmail4")
    PASSWORD = (By.NAME, "password")
    COMPANY = (By.NAME, "company")
    WEBSITE = (By.NAME, "website")

    COUNTRY = (By.NAME, "country")

    CITY = (By.NAME, "city")
    ADDRESS1 = (By.NAME, "address_line1")
    ADDRESS2 = (By.NAME, "address_line2")
    STATE = (By.ID, "inputState")
    ZIP = (By.ID, "inputZip")

    SUBMIT_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Submit')]"
    )

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        ".success-msg"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def enter_name(self, name):
        self.wait_for_element(self.NAME).send_keys(name)

    def enter_email(self, email):
        self.wait_for_element(self.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.wait_for_element(self.PASSWORD).send_keys(password)

    def enter_company(self, company):
        self.wait_for_element(self.COMPANY).send_keys(company)

    def enter_website(self, website):
        self.wait_for_element(self.WEBSITE).send_keys(website)

    def select_country(self, country):
        Select(
            self.wait_for_element(self.COUNTRY)
        ).select_by_visible_text(country)

    def enter_city(self, city):
        self.wait_for_element(self.CITY).send_keys(city)

    def enter_address1(self, address):
        self.wait_for_element(self.ADDRESS1).send_keys(address)

    def enter_address2(self, address):
        self.wait_for_element(self.ADDRESS2).send_keys(address)

    def enter_state(self, state):
        self.wait_for_element(self.STATE).send_keys(state)

    def enter_zip(self, zipcode):
        self.wait_for_element(self.ZIP).send_keys(zipcode)

    def click_submit(self):
        self.wait_for_element(
            self.SUBMIT_BUTTON
        ).click()

    def get_success_message(self):
        return self.wait_for_element(
            self.SUCCESS_MESSAGE
        ).text