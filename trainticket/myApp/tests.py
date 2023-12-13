import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class RouteFormSeleniumTest(unittest.TestCase):
    def setUp(self):
        # Assuming you have ChromeDriver installed and its executable in the system's PATH
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_add_route_form(self):
        # Open the form page
        self.driver.get("http://127.0.0.1:8000/add_route/")  # Replace with the actual URL of your form

        # Fill in the form fields
        self.driver.find_element_by_id("departure_time").send_keys("12:00 PM")
        self.driver.find_element_by_id("destination_station").send_keys("DestinationStation")

        # Add a route entry
        self.driver.find_element_by_class_name("add-route").click()

        # Wait for the dynamically added input fields to appear
        time.sleep(1)

        # Fill in the additional route entry fields
        route_stations = self.driver.find_elements_by_name("route_stations[]")
        route_stations[-1].send_keys("Station2")

        departure_times = self.driver.find_elements_by_name("departure_times[]")
        departure_times[-1].send_keys("01:00 PM")

        fare_amounts = self.driver.find_elements_by_name("fare_amounts[]")
        fare_amounts[-1].send_keys("50")

        # Fill in the remaining form fields
        self.driver.find_element_by_id("arrival_station").send_keys("ArrivalStation")

        # Submit the form
        self.driver.find_element_by_css_selector("button.btn-primary").click()

        # Wait for the form to submit (adjust the time as needed)
        time.sleep(1)

        # Assert that the form submission was successful (modify the assertion as needed)
        self.assertIn("Success", self.driver.page_source)

if __name__ == "__main__":
    unittest.main()
