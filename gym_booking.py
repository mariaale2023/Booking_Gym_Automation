# Loads the main Selenium WebDriver module to launch and control the browser
from selenium import webdriver
## create a new instance of the webdriver class with additional Service. This class represents the web browser that will be used to run your tests. In this example, you'll be using the Chrome web browser, so you need to create a new instance of the Chrome class, and the Service class described above allows web drivers to run a browser instance with additional capabilities.
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

# set up the Chrome web driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# open the web page
driver.get('https://recandsport.ccc.govt.nz/timetables/workout-timetables/')

# wait for the page to load
time.sleep(3)

# close the browser
driver.quit()

