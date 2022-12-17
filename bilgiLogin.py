from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Create an instance of the webdriver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://sis.bilgi.edu.tr/")

# Find the username and password fields
username_field = driver.find_element_by_id("mhd.khalifa@gmail.com")
password_field = driver.find_element_by_id("mohjammad0")

# Enter your login credentials
username_field.send_keys("your_username")
password_field.send_keys("your_password")

# Submit the login form
driver.find_element_by_css_selector(".btn-primary").click()

# If there is a reCAPTCHA, solve it
if driver.find_elements_by_css_selector(".g-recaptcha"):
  # Switch to the frame containing the reCAPTCHA
  driver.switch_to.frame(driver.find_element_by_css_selector(".g-recaptcha iframe"))

  # Click on the checkbox
  driver.find_element_by_css_selector(".recaptcha-checkbox-border").click()