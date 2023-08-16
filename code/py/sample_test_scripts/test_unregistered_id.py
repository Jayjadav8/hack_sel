import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

options = Options()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


class TestUnregisteredUID():
  ''' 
    Test login with an unregistered UID & PWD.

      Procedure:
      1. Go to the browser app.
      2. Click on sign in.
      3. Provide wrong UI & PWD on the login screen.
      4. Check if the login failed after the roundtrip to the server.

      Expected Outcome: The login should fail.
  '''
  
  def setup_method(self, method):
    '''Set up the test environment before each test method runs
    - webdriver.Chrome class is used to create an instance of the Chrome browser driver.
    '''
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    '''
    - Clean up after each test method finishes.
    - self.driver.quit() is called.
    - This command tells Selenium to close and quit the web browser and release any associated resources.
    '''
    self.driver.quit()

  def test_unregestered_user_id_and_password(self):
    '''steps for insertion of user name and password and then keycloak verify that 
    user name and password are not registered and throw input error'''

    filename = os.path.basename(__file__)
    # Remove the file extension from the filename
    test_name = os.path.splitext(filename)[0]

    # Create a directory for storing the screenshots if it doesn't exist
    screenshots_directory = "../screenshot"
    test_directory = os.path.join(screenshots_directory, test_name)
    if not os.path.exists(test_directory):
        os.makedirs(test_directory)

    #Step 1:
    self.driver.get("https://qbrow.rasree.com/")
    expected_title = "Home | Rasree"
    assert expected_title in self.driver.title, f"Page title '{self.driver.title}'\
        does not match expected title '{expected_title}'"

    self.driver.set_window_size(1440, 804)
    #Step 2
    self.driver.find_element(By.CSS_SELECTOR, ".kjsDg > .bWxOKe").click()
    #Step 3
    
    #TODO break it up into elemental steps like done to usernameTxt
    screenshot_filename = f"{test_name}_screenshot_explorepage.png"
    screenshot_path = os.path.join(test_directory, screenshot_filename)
    self.driver.get_screenshot_as_file(screenshot_path)

    usernameTxt=self.driver.find_element(By.ID, "username")
    assert usernameTxt is not None
    assert usernameTxt.tag_name == "input"

    time.sleep(5)

    self.driver.find_element(By.ID, "username").send_keys("anadi")
    self.driver.find_element(By.ID, "password").click()

    time.sleep(5)

    self.driver.find_element(By.ID, "password").send_keys("mishra")
    self.driver.find_element(By.ID, "kc-login").click()
    
    time.sleep(5)

    #Step 4
    # The page should do a roundtrip to server:
    #TODO: do we need to sleep for a bit?
    # Test assertion: the page should have a span with id: input-error and 
    # its text should contain: "Invalid username or password."
    invalid_span = self.driver.find_element(By.ID, "input-error")
    # assert invalid_span is not None 
    # #TODO: check if invalid_span is of type span
    
    
    # assert invalid_span.tag_name == "span"

    # pytest. assertIn("Invalid username or password.", invalid_span.text)
    messsage = "Invalid username or password."
    assert messsage == invalid_span.text 
