# pyright: reportGeneralTypeIssues= false, reportUnknownMemberType= false
# pyright: reportOptionalMemberAccess= false, reportUnboundVariable = false
# pyright: reportUnknownArgumentType= false, reportUnknownVariableType= false
# pyright: reportUnknownParameterType= false, reportMissingTypeArgument= false
# pyright: reportMissingTypeStubs= false

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException, TimeoutException, \
    InvalidArgumentException, InvalidElementStateException


class BrowserAppSteps:
    '''
    A class representing browser app steps.
        Attributes:
            driver: The driver instance for the browser.
            browser_name (str): The name of the browser.
            browser_server_url (str): The server URL for the browser.
            duration (int): The duration of the app steps.
            comic_out_folder (str): The output folder for comic files.
    '''

    driver= None
    browser_name= None 
    browser_server_url= None
    duration= 10


    def __init__(self, browser:str= None, browser_server_url:str=None, duration: int = 10):
        '''
          Initializes the BrowserAppSteps object.

        Args:
            browser (str): The name of the browser.
            browser_server_url (str): The server URL for the browser.
            duration (int): The duration of the app steps.
        
        '''
        self.browser_name= browser
        self.browser_server_url= browser_server_url
        self.duration = duration
        if self.browser_name is None or self.browser_server_url is None:
            print("FATAL: Useless to create class without browser and server")
            sys.exit(1)
        else:
            self.setUp(self.browser_name, self.browser_server_url, self.duration)
        current_date_time=datetime.now()
        date_time_string = current_date_time.strftime("%Y-%m-%d-%H-%M-%S")
        self.comic_out_folder="comic-"+date_time_string+"/"


    def setUp(self, browser:str, browser_server:str, duration: int):
    
        '''Set up the test environment before each test method runs
        - webdriver.Chrome class is used to create an instance of the Chrome browser driver.
        Args:
            browser (str): The name of the browser.
            browser_server (str): The server URL for the browser.
            duration (int): The duration of the app steps.
        '''

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(duration)

        if self.driver is None:
            print("FATAL: Driver could not be initialized ")
            sys.exit(1)


    def visit_page(self, url: str, wait: str, duration: int, scrshot: bool, checks: dict, exit_element: dict, 
        screenshot_path: str= None, screen_shot_name: str=None, wait_el_id: str = None):
        '''This function will get driver to unsigned page and check's required element presense
        param url: browser app url
        param wait: wait type like implicit, explicit wait
        param duration: webdriver wait time 
        param scrshot: optin for screenshot required or not. it will be in boolean true means take screenshot else don't take
        param checks: check's is a dict. it contains elements should to be present in the page 
        param exit_element: this contains hook element to the next page 
        param screenshot_path: this containes path where screenshots will be stored 
        param screen_shot_name: name of the screenshot
        param wait_el_id: this element used to pause driver, The pause lets the page load and the web elements become 
        visible/present/clickable before WebDriver can interact with 
        return type : dict 
        return's    : check_result, step_error
        '''
        step_error_list=""
        step_error=""
        check_result={}
        proceed=True
        pageload_time = None
        try:
            self.driver.get(url)
            pageload_time= self.web_page_load_time()
        except TimeoutException as e:
            step_error="FATAL: Page not Found\n"
            print("step error: ",step_error)
            print(e.with_traceback)
            proceed=False
        except Exception as e: #TODO: keep this under watch for more possible errors.
            step_error="FATAL: In visit page, Unhandled Exception, see printed log\n"
            print("step error: ",step_error)
            print(e)
            proceed=False
        step_error_list+= step_error
        check_result, step_error_list = self.load_page(proceed, wait, duration, scrshot, \
            checks, exit_element, step_error_list,check_result,
        screenshot_path, screen_shot_name, wait_el_id)
        
        return check_result, pageload_time, step_error_list

