from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome webdriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://thinking-tester-contact-list.herokuapp.com/")

try:
    # Find the username and password input fields and enter values
    username_field = driver.find_element_by_id("email")
    password_field = driver.find_element_by_id("password")
    username_field.send_keys("vamsikana1@gmail.com")
    password_field.send_keys("oggy123456")

    # Find the login button by its ID and click it
    login_button = driver.find_element_by_id("submit")
    login_button.click()

    # Wait for the welcome message to be visible after login
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "welcome-message"))
    )

    # If the element is found, print a success message
    print("Test Passed: Login successful!")

except Exception as e:
    # If any exception occurs or the element is not found, print an error message
    print("Test Failed: ", e)

finally:
    # Close the browser window
    driver.quit()
