from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import os

def test_correct_url(self): 
    self.driver.get("https://qbrow.rasree.com/")
    # 2 | setWindowSize | 1440x805 | 
    self.driver.set_window_size(1440, 805)

    expected_title = "Home | Rasree"
    assert expected_title in self.driver.title, f"Page title '{self.driver.title}'\
        does not match expected title '{expected_title}'"
    self.capture_screenshot("Step_2_Homepage")


def inputExploreBtn(self):
    """
    Clicks on the 'inputExploreBtn' element on the page and verifies the page title.

    Returns:
        tuple: A tuple containing two values:
            - details (str): Contains either an error message or a message confirming the page title match.
            - result (bool): True if the page title matches the expected title, False otherwise.
    """

    # Click on the 'inputExploreBtn' element
    self.driver.find_element(By.ID, "inputExploreBtn").click()

    # Define the expected title
    expected_title = "Explore | Rasree"

    # Get the actual title of the page
    actual_title = self.driver.title

    # Check if the actual title matches the expected title
    if expected_title not in actual_title:
        details = f"Page title '{actual_title}' does not match expected title '{expected_title}'"
        result = False
    else:
        details = f"Page title '{actual_title}' matches expected title '{expected_title}'"
        result = True

    return details, result
