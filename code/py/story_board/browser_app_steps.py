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
import time
import traceback



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


    def web_page_load_time(self):
        '''
        Calculate the web page loading time using the performance timing API.

        Returns:
            float: The time taken for the web page to load in seconds.
        '''

        # Retrieve the response start time and DOM load completion time from the performance timing API.
        responseStart = self.driver.execute_script("return window.performance.timing.responseStart")
        domComplete = self.driver.execute_script("return window.performance.timing.domComplete")

        # Calculate the time taken for the web page to load by subtracting 
        # response start time from DOM load completion time.
        # The result is divided by 1000 to convert milliseconds to seconds.
        return float(domComplete - responseStart) / 1000


    def visit_page(self, url: str, wait_type: str, implicit_wait_duration: int, \
            scr_shot_needed: bool, current_page_check_elements: dict, page_exit_element: dict, 
        screenshot_path: str= None, screen_shot_name: str=None, wait_element_id: str = None):
        '''
        Visits a page in the browser app, checks required elements' presence,
          and takes screenshots if specified.
        
        Args:
            url (str): The URL of the page to visit in the browser app.
            wait (str): The type of wait to apply during the page load (implicit, explicit, or fluent).
            duration (int): The duration of the WebDriver wait time in seconds.
            scr_shot_needed (bool): Whether to take a screenshot (True) or not (False).
            checks (dict): A dictionary containing elements that should be present on the page.
            exit_element (dict): A dictionary representing the exit element to proceed to the next page.
            screenshot_path (str, optional): The path where screenshots will be stored. Default is None.
            screenshot_name (str, optional): The name of the screenshot. Default is None.
            wait_el_id (str, optional): The element used to pause the driver to wait for page elements to load.
                                        Default is None.

            Returns:
                dict: A dictionary containing check results and other information.
                    - check_result: A dictionary containing the results of the checks performed on the page.
                    - pageload_time: The time taken for the page to load in seconds.
                    - step_error_list: A string containing any errors that occurred during the page visit and checks.
                
        '''
        step_error_list=""
        step_error=""
        can_proceed_ahead=True
        page_load_time = None

        try:
            self.driver.get(url)
            page_load_time= self.web_page_load_time()

        except TimeoutException as e:
            step_error="FATAL: Page not Found\n"
            can_proceed_ahead=False

        except Exception as e:
            step_error="FATAL: In visit page, Unhandled Exception, see printed log\n"
            can_proceed_ahead=False

        # String containing errors if Exception occurs.
        step_error_list+= step_error

        # Inserting required values to load_page() function
        check_element_present_result, all_step_error_list = \
            self.load_page(can_proceed_ahead, wait_type,
                implicit_wait_duration, scr_shot_needed,\
                current_page_check_elements, page_exit_element,\
                step_error_list, screenshot_path,
                screen_shot_name, wait_element_id)
        
        return check_element_present_result, page_load_time, all_step_error_list



    def load_page(self, can_proceed_ahead: bool, wait_type: str, implicit_wait_duration: int,\
        scr_shot_needed: bool,current_page_check_elements: dict, page_exit_element: dict, step_error_list:str,
        screenshot_path: str= None, screen_shot_name: str=None, 
        wait_element_id: str = None, screenshot_delay: int =2):

        '''
        Perform tasks like taking a screenshot, checking elements, and 
        collecting errors if any occur during page loading.
        
        Args:
            proceed (bool): Whether to proceed with the page checks.
            wait (str): The type of wait to apply during the page load (implicit, explicit, or fluent).
            duration (int): The duration of the WebDriver wait time in seconds.
            scr_shot_needed (bool): Whether to take a screenshot (True) or not (False).
            page_checks (dict): A dictionary containing elements that should be present on the page.
            exit_element (dict): A dictionary representing the exit element to proceed to the next page.
            step_error_list (str): A string containing any errors that occurred during the page visit and checks.
            check_result (dict): A dictionary to store the results of the checks performed on the page.
            screenshot_path (str, optional): The path where screenshots will be stored. Default is None.
            screenshot_name (str, optional): The name of the screenshot. Default is None.
            wait_el_id (str, optional): The element used to pause the driver to wait for page elements to load.
                                        Default is None.
            sl_time (int, optional): Time in seconds to sleep before taking a screenshot. Default is 2.

        Returns:
             A Dictionary containing the updated check results dictionary and the updated step_error_list.
    
            '''

        step_error=""
        check_element_present_result = {}

        if not can_proceed_ahead:
            return check_element_present_result, step_error_list  # Early return if proceed is False

        if wait_type is not None:
            try:
                if wait_type == "implicit":
                    self.driver.implicitly_wait(implicit_wait_duration)
                
                elif wait_type == "explicit":
                    wait = WebDriverWait(self.driver, implicit_wait_duration)
                    wait.until(EC.presence_of_element_located((By.ID,wait_element_id)))

            except NoSuchElementException as e:
                can_proceed_ahead = False
                step_error=f"FATAL: No Element named {wait_element_id} found after {implicit_wait_duration}\n"

            except Exception as e:
                step_error+= f"FATAL: Unhandled exception stoping step execution: {e}\n"
                traceback.print_exc()
                can_proceed_ahead = False

        if not can_proceed_ahead:
            return check_element_present_result, step_error_list  # Early return if proceed is False

        if scr_shot_needed:
            time.sleep(screenshot_delay)
            can_proceed_ahead, step_err = self.take_screenshot(screenshot_path,\
                                             screen_shot_name, step_error)
            step_error+= step_err

        if not can_proceed_ahead:
            return check_element_present_result, step_error_list  # Early return if proceed is False

        for element_key, element_data in current_page_check_elements.items():

            if 'id' not in element_data:
                step_error += f"Element {element_key}: 'id' key is missing."
                can_proceed_ahead= False

            elif not element_data['id'].strip():
                step_error += f"Element {element_key}: 'id' value is an empty string."
                can_proceed_ahead= False

            try:
                wait = WebDriverWait(self.driver, implicit_wait_duration)
                wait.until(EC.presence_of_element_located((By.ID,wait_element_id)))
                check_element_present_result[element_key]["found"] = True
                    
            except NoSuchElementException as e:
                step_error+=f"FATAL: No Element named {element_key} found\n"
                can_proceed_ahead= False


            except Exception as e:
                step_error+= f"FATAL: Unhandled exception stoping step execution: {e}\n"
                traceback.print_exc()
                can_proceed_ahead = False
            

        if not can_proceed_ahead:
            return check_element_present_result, step_error_list  # Early return if proceed is False
            
        element_id= page_exit_element['id']

        try:
            wait = WebDriverWait(self.driver, implicit_wait_duration)
            wait.until(EC.presence_of_element_located((By.ID,element_id)))
            check_element_present_result[element_id]= {}
            check_element_present_result[element_id]["found"]=True

        except NoSuchElementException as e:
            step_error+=f"No Element named {element_id} found\n"

        except Exception as e:
            step_error+=f"FATAL: Unhandled exception stoping step execution: {e}\n"
            traceback.print_exc()
            can_proceed_ahead= False

        step_error_list+= step_error
        return check_element_present_result, step_error_list



    def take_screenshot(self, screenshot_path_folder:str, screen_shot_name:str, step_error_list: str):
        '''
        Take a screenshot of the web page and save it.

        Args:
            screenshot_path_folder (str): The name of the directory where screenshots should be stored.
            screen_shot_name (str): The name of the screenshot file.
            step_error_list (str): A string containing any errors that occurred during the step.

        Returns:
             boolean (proceed) indicating whether the screenshot was taken successfully,
                and the updated step_error_list with any new errors.
        '''

        can_proceed_ahead = True
        step_error= ""
        
        try:
        
            screenshots_directory = screenshot_path_folder
            test_directory = os.path.join(screenshots_directory, screen_shot_name)
            if not os.path.exists(test_directory):
                os.makedirs(test_directory)
            
            self.driver.save_screenshot(os.path.join(test_directory, screen_shot_name))
        
        except FileNotFoundError as e:
            step_error+= f'FATAL: Storyboard screenshot {screenshot_path_folder} not found, cannot move forward {e}\n'
            can_proceed_ahead= False
        
        except PermissionError as e:
            step_error+=f"FATAL: You don't have write permission to write {screenshot_path_folder + screen_shot_name}\n"
            can_proceed_ahead= False
        
        except Exception as e:
            step_error+=f"FATAL: Unhandled exception stoping step execution: {e}\n"
            traceback.print_exc()
            can_proceed_ahead= False
        
        step_error_list+= step_error
        return can_proceed_ahead, step_error_list

