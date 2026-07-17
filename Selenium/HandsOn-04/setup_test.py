"""
Hands-On 4
Task 2
Navigation, Tabs, Screenshot & Window Size
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/")

# Click Simple Form Demo
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

# Verify URL
assert "simple-form-demo" in driver.current_url

print("URL Verified")

# Go Back
driver.back()

# Open New Tab
driver.execute_script('window.open("https://www.google.com");')

# Print all handles
print(driver.window_handles)

# Switch to Google Tab
driver.switch_to.window(driver.window_handles[1])

print("Google Title:")
print(driver.title)

# Switch back
driver.switch_to.window(driver.window_handles[0])

# Screenshot
driver.save_screenshot("playground_screenshot.png")

print("Screenshot Saved")

# Current Window Size
print("Current Window Size:")
print(driver.get_window_size())

# Consistent window size is important because responsive websites
# change layouts based on browser dimensions. Keeping a fixed size
# ensures reliable and repeatable automation tests.

driver.set_window_size(1280, 800)

print("New Window Size:")
print(driver.get_window_size())

driver.quit()