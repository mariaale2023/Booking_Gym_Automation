from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Scroll helper function
def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.set_window_size(1280, 1024)

# Open the target page
driver.get('https://recandsport.perfectgym.com/ClientPortal2/#/Classes/2/List?categoryId=1')

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



# Optional pause for visual confirmation
time.sleep(8)

# Close the browser
driver.quit()
