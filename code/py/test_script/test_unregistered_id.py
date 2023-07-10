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
options = Options()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


class TestTestingP2():
  ''' 
  DESCRIPTION: This test trys to login with an unregistered UID & PWD
  PROCEDURE: 
  1. go to browser app
  2. click on sign in
  3. provide wrong UI & PWD on login screen
  4. check if the login failed after the roundtrip to server
  EXPECTED OUTCOME: The login should fail
  '''
  def setup_method(self, method):
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testingP2(self):
    '''steps for insertion of user name and password and then keycloak verify that 
    user name and password are not registered and throw input error'''
    #Step 1:
    self.driver.get("https://qbrow.rasree.com/")
    self.driver.set_window_size(1440, 804)
    #Step 2
    #TODO: get an id for signin button @somanath
    self.driver.find_element(By.CSS_SELECTOR, ".kjsDg > .bWxOKe").click()
    #TODO: do we need to sleep? New page loads
    #Step 3
    #TODO break it up into elemental steps like done to usernameTxt
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
