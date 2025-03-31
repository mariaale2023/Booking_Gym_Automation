#import .env file

from dotenv import load_dotenv
import os

#import Selenium packeges
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Load the environment variables
load_dotenv()


BASE_URL = os.getenv("BASE_URL")
USERNAME = os.getenv("NAME")
PASSWORD = os.getenv("PASSWORD")
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH")   

print("username:", os.getenv("USERNAME"))
print("DEBUG - USERNAME:", repr(USERNAME))

# Scroll helper function
def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.set_window_size(1280, 1024)

# Open the target page
driver.get(BASE_URL)

# # Wait for the button's text to appear on the page
# wait = WebDriverWait(driver, 15)
# wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Change facility"))


# # Find and click the "Change Facility" button
# buttons = driver.find_elements(By.TAG_NAME, "button")
# for button in buttons:
#     if "Change facility" in button.text:
#         scroll_to_element(driver, button)
#         time.sleep(1)
#         button.click()
#         break

# step 1: Click "Change Facility" buttom
change_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "baf\\:button.cp-choose-club-desktop.baf-button"))
)
change_button.click()
print("change button clicked")

# Step 2: Wait until the dropdown becomes visible
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".cp-choose-club.dropdown-visible"))
)

# Wait for and click the desired facility
facility_name = "Pioneer Recreation and Sport Centre"  # Change as needed
facility_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{facility_name}')]"))
)
facility_button.click()
print("facility button clicked")


# click on sing in button
sign_in_button = WebDriverWait(driver, 15).until(
#    EC.element_to_be_clickable((By.CSS_SELECTOR, "//span[contains(@class, 'cp-btn' and text(), ' Sign in ')]"))
#    EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'cp-btn' and text(), ' Sign in ')]"))
    EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(), 'Sign in')]"))
)
sign_in_button.click()
print("sign in button clicked")

# -- Wait for the login form to appear
## Add user name
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Login']"))
)
username_input.click()
username_input.clear()
time.sleep(5)
print("Username being sent:", USERNAME)



#username_input.send_keys(USERNAME)  # needs go to variables
username_input.send_keys(USERNAME)  # needs go to variables

## Add password
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Password']"))
)
password_input.clear()
password_input.send_keys(PASSWORD)  # variables

## Click on the login button
login_button = WebDriverWait(driver, 10).until(
   # EC.element_to_be_clickable((By.CSS_SELECTOR, "baf\\:button.cp-btn-next.cp-login-btn-login.baf-button']"))
   # EC.element_to_be_clickable((By.CSS_SELECTOR, "baf\\:button.confirm.cp-btn-next.cp-login-btn-login.baf-button']"))
   # EC.element_to_be_clickable((By.CSS_SELECTOR, "baf\\:button#confirm']"))

   # EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='auth-form-actions']"))
    # EC.element_to_be_clickable(By.XPATH, f"//span[contains(text(), 'glyphicon')]")
    # EC.element_to_be_clickable((By.XPATH, "//baf:button[icon='cp-button-right']"))
    # EC.element_to_be_clickable((By.XPATH, "//baf:button[id='confirm']"))
    # EC.element_to_be_clickable((By.XPATH, "//baf:button[@id='confirm']"))
     EC.element_to_be_clickable((By.XPATH, "//*[@id='confirm']"))
)
driver.execute_script("arguments[0].click();", login_button)
#login_button.click() #dont click twice the buttom

print("login button clicked")



# Optional pause for visual confirmation
time.sleep(8)

# Close the browser
driver.quit()
