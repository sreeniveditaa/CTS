from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    )
)

driver.maximize_window()

driver.get(
    "https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo"
)

button = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//button[contains(text(),'Autoclosable Success Message')]"
        )
    )
)

button.click()

print("Button Clicked Successfully")

start = time.time()

alert = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located(
        (
            By.CSS_SELECTOR,
            ".alert-success"
        )
    )
)

end = time.time()

print("\nExplicit Wait Time:")
print(end-start)

assert "success" in alert.text.lower()

print("\nAlert Text:")
print(alert.text)

start = time.time()

time.sleep(3)

end = time.time()

print("\nTime Sleep:")
print(end-start)

# Note:
# The current version of the LambdaTest Bootstrap Alerts page
# does not contain a dynamically loaded table.
# Therefore, Fluent Wait is demonstrated using the success alert
# to show the same waiting concept.

wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5,
    ignored_exceptions=[NoSuchElementException]
)

success_alert = wait.until(
    EC.visibility_of_element_located(
        (
            By.CSS_SELECTOR,
            ".alert-success"
        )
    )
)

print("\nFluent Wait Successful")
print(success_alert.text)

driver.quit()