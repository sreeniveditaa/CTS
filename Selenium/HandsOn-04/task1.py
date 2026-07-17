"""
Hands-On 4
Selenium WebDriver Setup, Browser Drivers & Basic Commands

Selenium Components:

1. WebDriver
   - WebDriver is the main component used to automate browsers.
   - It communicates with the browser using browser-specific drivers
     like ChromeDriver.

2. Selenium Grid
   - Selenium Grid allows tests to run on multiple browsers,
     operating systems and machines simultaneously.
   - It helps in parallel execution and reduces execution time.

3. Selenium IDE
   - Selenium IDE is a browser extension.
   - It is mainly used for record and playback of test cases.
   - It can also generate automation scripts.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Chrome options
options = webdriver.ChromeOptions()

# Run browser in headless mode
options.add_argument("--headless")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Implicit Wait
# Implicit wait is generally not preferred because it applies globally
# to all elements and may increase execution time.
# Explicit waits are more efficient because they wait only for
# specific elements.

driver.implicitly_wait(10)

driver.get("https://www.lambdatest.com/selenium-playground/")

print("Page Title:")
print(driver.title)

driver.quit()