from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = r"C:\Windows\System32\chromedriver-win64\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Specify path to Chrome binary if needed
chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://thinking-tester-contact-list.herokuapp.com/")

try:
    username_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys("oggy@gmail.com")
    password_field.send_keys("oggy123456")

    login_button = driver.find_element(By.ID, "submit")
    login_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "add-contact"))
    )

    add_contact_button = driver.find_element(By.ID, "add-contact")
    add_contact_button.click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "add-contact"))
        )
    
    name_field = driver.find_element(By.ID, "firstName")
    name2_field = driver.find_element(By.ID,"lastName")
    email_field = driver.find_element(By.ID, "email")
    dob_field = driver.find_element(By.ID, "birthdate")
    phone_field = driver.find_element(By.ID, "phone")
    address_field = driver.find_element(By.ID, "street1")

    name_field.send_keys("Cheeku")
    name2_field.send_keys("Bhaiya")
    email_field.send_keys("runmachine18@gmail.com")
    dob_field.send_keys("1984-12-30")
    phone_field.send_keys("6365789461")
    address_field.send_keys("Delhi,India")

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myTable"))
        )
    
    contact_add = driver.find_element(By.ID,"myTable")
    screenshot2 = contact_add.screenshot("result.png")
    screenshot2 = Image.open("result.png")
    screenshot2.show()
    print("Test Passed: Login successful!")

except Exception as e:
    print("Test Failed: ", e)

finally:
    driver.quit()
