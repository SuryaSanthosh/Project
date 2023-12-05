from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Initialize your WebDriver
        self.driver.get("http://127.0.0.1:8000/login/")  # Replace with your login page URL

    def test_valid_login(self):
        username = "sooraj"
        password = "sooraj"

        # Find username and password fields
        username_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "username"))  # Update with your username field locator
        )
        password_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "password"))  # Update with your password field locator
        )

        # Enter username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Trigger change events after entering username and password
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", username_field)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", password_field)

        # Find and click the login button
        login_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, "login-button"))  # Update with your login button locator
        )
        login_button.click()

        # Add assertions to verify successful login
        expected_url = "/home/"
        self.assertIn(expected_url, self.driver.current_url)  # Update with assertion to check if expected_url is present in the current URL
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    # Your main code here

    unittest.main()