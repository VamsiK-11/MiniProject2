from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "C:\Windows\System32\chromedriver-win64\chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"  # Specify path to Chrome binary if needed
chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://thinking-tester-contact-list.herokuapp.com/")

try:
    username_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys("vamsikana1@gmail.com")
    password_field.send_keys("oggy123456")

    login_button = driver.find_element(By.ID, "submit")
    login_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "add-contact"))
    )

    print("Test Passed: Login successful!")

except Exception as e:
    print("Test Failed: ", e)

finally:
    driver.quit()
