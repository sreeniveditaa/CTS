from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

print("Website Opened Successfully\n")

message = driver.find_element(By.ID, "user-message")
print("✅ ID Locator Successful")

try:
    message = driver.find_element(By.NAME, "message")
    print("✅ Name Locator Successful")
    print("Located Element:")
    print(message.get_attribute("outerHTML"))
except:
    print("❌ Name Locator not applicable for the current textbox.")

message = driver.find_element(
    By.CLASS_NAME,
    "border"
)

print("✅ Class Name Locator Successful")

message = driver.find_element(
    By.TAG_NAME,
    "input"
)

print("✅ Tag Name Locator Successful")

print("✅ Absolute XPath (Example Only)")

message = driver.find_element(
    By.XPATH,
    "//input[@id='user-message']"
)

print("✅ Relative XPath Successful")

message = driver.find_element(
    By.CSS_SELECTOR,
    "#user-message"
)

print("✅ CSS Selector (ID) Successful")

message = driver.find_element(
    By.CSS_SELECTOR,
    "input[placeholder='Please enter your Message']"
)

print("✅ CSS Selector (Attribute) Successful")


message = driver.find_element(
    By.CSS_SELECTOR,
    "div.left-input input"
)

print("✅ CSS Selector (Parent Child) Successful")



driver.quit()

print("\nAll locator strategies executed successfully.")