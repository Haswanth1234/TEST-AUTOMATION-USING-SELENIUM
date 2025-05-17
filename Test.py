from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# ✅ Step 2: Correct path to chromedriver.exe
service = Service("D:\chromedriver-win64\chromedriver-win64\chromedriver.exe")  # Update path if needed

# ✅ Step 3: Pass Service object to Chrome
driver = webdriver.Chrome(service=service)

# ✅ The rest of your code
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

if "Logged In Successfully" in driver.page_source:
    print("Login successful!")
else:
    print("Login failed.")

driver.quit()
