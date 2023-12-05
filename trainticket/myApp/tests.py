from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome WebDriver (replace 'path/to/chromedriver' with the actual path)
driver = webdriver.Chrome(executable_path='path/to/chromedriver')

# Navigate to the login page
driver.get('http://127.0.0.1:8000/login/')  # Replace with the actual URL

# Find the username and password input fields
username_input = driver.find_element_by_name('username')
password_input = driver.find_element_by_name('password')

# Input valid or invalid credentials
username_input.send_keys('sooraj')
password_input.send_keys('sooraj')

# Submit the form
password_input.send_keys(Keys.RETURN)

# Wait for a moment to allow the page to load (you might need to adjust the sleep duration)
time.sleep(2)

# Check for successful login or error message
if 'successful_login_indicator' in driver.current_url:  # Replace with an indicator of successful login
    print('Login successful!')
else:
    error_message = driver.find_element_by_id('error-message').text  # Replace with the actual error message element ID
    print(f'Login failed. Error message: {error_message}')

# Close the browser
driver.quit()
