from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import pytest

@pytest.mark.parametrize(
    "message",
    [
        "Hello",
        "Selenium Automation",
        "12345"
    ]
)
def test_simple_form_submission(driver, base_url, message):

    driver.get(base_url + "simple-form-demo")

    textbox = driver.find_element(By.ID, "user-message")

    textbox.clear()

    textbox.send_keys(message)

    driver.find_element(By.ID, "showInput").click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "message"))
    )

    output = driver.find_element(By.ID, "message")

    print("Displayed:", output.text)


def test_checkbox_demo(driver):

    driver.get(
        "https://www.lambdatest.com/selenium-playground/checkbox-demo"
    )

    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[type='checkbox']")
        )
    )

    checkbox.click()

    assert checkbox.is_selected()

    checkbox.click()

    assert not checkbox.is_selected()