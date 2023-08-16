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
import yaml
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import traceback
from typing import Dict, Any
from mdutils import MdUtils


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


    def __init__(self, browser:str, browser_server_url:str):
        '''
          Initializes the BrowserAppSteps object.

        Args:
            browser (str): The name of the browser.
            browser_server_url (str): The server URL for the browser.
            driver_wait_duration (int): The duration of the app steps.
        
        '''
        driver_wait_duration = 10
        self.browser_name= browser
        self.browser_server_url= browser_server_url
        # self.driver_wait_duration = driver_wait_duration
        if self.browser_name is None or self.browser_server_url is None:
            print("FATAL: Useless to create class without browser and server")
            sys.exit(1)
        else:
            self.setUp(self.browser_name, self.browser_server_url, driver_wait_duration)

    def setUp(self, browser:str, browser_server:str, driver_wait_duration: int):
    
        '''Set up the test environment before each test method runs
        - webdriver.Chrome class is used to create an instance of the Chrome browser driver.
        Args:
            browser (str): The name of the browser.
            browser_server (str): The server URL for the browser.
            duration (int): The duration of the app steps.
        '''
        options = Options()

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        self.driver.implicitly_wait(driver_wait_duration)

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


    def visit_page_to_be_tested_in_step(self,step_input_data_dict:dict):

        '''
        Visits a page in the browser app, checks required elements' presence,
          and takes screenshots if specified.
        
        Args:
            step_input_data(dict) contains fiollowing :
                url (str): The URL of the page to visit in the browser app.
                wait (str): The type of wait to apply during the page load (implicit, explicit, or fluent).
                duration (int): The duration of the WebDriver wait time in seconds.
                scr_shot_needed (bool): Whether to take a screenshot (True) or not (False).
                checks (dict): A dictionary containing elements that should be present on the page.
                exit_element (dict): A dictionary representing the exit element to proceed to the next page.
                screenshot_path (str, optional): The path where screenshots will be stored. Default is None.
                screenshot_name (str, optional): The name of the screenshot. Default is None.
        
                Returns:
                dict: A dictionary containing check results and other information.
                    - check_result: A dictionary containing the results of the checks performed on the page.
                    - pageload_time: The time taken for the page to load in seconds.
                    - step_error_list: A string containing any errors that occurred during the page visit and checks.
                
        '''

        page_url = str(step_input_data_dict["page_url"])

        # Store errors/exception in dictionary step_error_dict if occurs.
        visit_function_step_error_dict= {}
        step_error=""
        check_element_present_result = {}
        
        can_proceed_ahead=True
        page_load_time = step_input_data_dict["page_load_time"]

        try:
            self.driver.get(page_url)
            self.driver.set_window_size(1440, 804)
    
            page_load_time= self.web_page_load_time()

        except TimeoutException as e:
            step_error="FATAL: Time out Exception has occur ,Page not Found\n"
            can_proceed_ahead=False
            visit_function_step_error_dict["visit_page_function"]= step_error
            traceback.print_exc()


        except Exception as e:
            step_error="FATAL: In visit page, Unhandled Exception has occur \n"
            can_proceed_ahead=False
            visit_function_step_error_dict["visit_page_function"]= step_error
            traceback.print_exc()

        # Early return if can_proceed_ahead is False
        if not can_proceed_ahead:
            return check_element_present_result,page_load_time ,visit_function_step_error_dict

        # Inserting required values to load_page() function
        check_element_present_result, load_page_function_step_error_dict = \
            self.load_page(step_input_data_dict)
        
        return check_element_present_result, page_load_time, load_page_function_step_error_dict
    
    def load_page(self,step_input_data_dict:dict):
        '''
        Perform tasks like taking a screenshot, checking elements, and 
        collecting errors if any occur during page loading.
        
        Args:
            proceed (bool): Whether to proceed with the page checks.
            step_input_data :dict , contains following keys
                wait (str): The type of wait to apply during the page load (implicit, explicit, or fluent).
                duration (int): The duration of the WebDriver wait time in seconds.
                scr_shot_needed (bool): Whether to take a screenshot (True) or not (False).
                page_checks (dict): A dictionary containing elements that should be present on the page.
                exit_element (dict): A dictionary representing the exit element to proceed to the next page.
                step_error_list (str): A string containing any errors that occurred during the page visit and checks.
                check_result (dict): A dictionary to store the results of the checks performed on the page.
                screenshot_path (str, optional): The path where screenshots will be stored. Default is None.
                screenshot_name (str, optional): The name of the screenshot. Default is None.
            wait_element_id (str, optional): The element used to pause the driver to wait for page elements to load.
                                        Default is None.
            screenshot_delay (int, optional): Time in seconds to sleep before taking a screenshot. Default is 2.

        Returns:
             A Dictionary containing the updated check results dictionary and the updated step_error_list.
    
            '''

        # Fetching data from dictionaryu to variable
        screenshot_needed = bool(step_input_data_dict["screenshot_needed"])
        screenshot_name = step_input_data_dict["screenshot_name"]
        screenshots_directory_path = step_input_data_dict["screenshots_directory_path"]

        implicit_wait_duration= step_input_data_dict["wait"]["implicit_type_duration"]
        current_page_element_to_be_tested_dict= step_input_data_dict["elements_to_be_tested"]

        # list of explicit wait elements id
        explicit_wait_elements_id_list = step_input_data_dict["wait"]["explicit_wait_elements_id_list"]
        explicit_wait_duration = step_input_data_dict["wait"]["explicit_type_duration"]
 
        # variable declaration in the function
        can_proceed_ahead = True
        step_error=""
        check_element_present_result = {}
        load_page_function_step_error_dict = {}
       
        
        # Implementing implicit wait on page.
        try:
            self.driver.implicitly_wait(implicit_wait_duration)
                
        except Exception as e:
            step_error+= f"FATAL: Unhandled exception stoping step execution: {e}\n"
            traceback.print_exc()
            can_proceed_ahead = False
            load_page_function_step_error_dict["load_page_function"] = step_error


        if not can_proceed_ahead:
            return check_element_present_result, load_page_function_step_error_dict  # Early return if can_proceed_ahead is False

        if screenshot_needed:
            step_name = step_input_data_dict["screenshot_name"]
            self.capture_screenshot(step_name,"visitPage")


        if not can_proceed_ahead:
            return check_element_present_result, load_page_function_step_error_dict  # Early return if can_proceed_ahead is False


        for element_key, element_data in current_page_element_to_be_tested_dict.items():

            # element_data example : element_1 , element_key example type,text and id
            if 'id' not in element_data:
                step_error += f"Element {element_key}: 'id' key is missing."
                can_proceed_ahead= False
                load_page_function_step_error_dict["load_page_function"] = step_error


            elif not element_data['id'].strip():
                step_error += f"Element {element_key}: 'id' value is an empty string."
                can_proceed_ahead= False
                load_page_function_step_error_dict["load_page_function"] = step_error

            try:    #  Test if element is presnt on page.

                wait_element_id = element_data['id']
                # checking if explicit wait need to be apply:
                if wait_element_id in explicit_wait_elements_id_list:
                    wait = WebDriverWait(self.driver, explicit_wait_duration)
                    wait.until(EC.presence_of_element_located((By.ID,wait_element_id)))
                
                check_element_present_result[element_key] ={}
                check_element_present_result[element_key]["found"] = True
                    
            except NoSuchElementException as e:
                step_error+=f"FATAL: No Element named {element_key} found\n"
                can_proceed_ahead= False
                load_page_function_step_error_dict["load_page_function"] = step_error


            except Exception as e:
                step_error+= f"FATAL: Unhandled exception stoping step execution: {e}\n"
                traceback.print_exc()
                can_proceed_ahead = False
                load_page_function_step_error_dict["load_page_function"] = step_error

        if not can_proceed_ahead:
            return check_element_present_result, load_page_function_step_error_dict  # Early return if proceed is False
            
        return check_element_present_result, load_page_function_step_error_dict


    def element_check_readable_response(self, step_input_data_dict: dict, \
            step_02_check_element_present_result: dict,\
            step_02_page_load_time:int):
        
        '''
         Get the comic out file content for a particular step.

        Args:
            step_name (str): The name of the step.
            step_image (str): The image of the particular step.
            step_page_load_time (str): The time taken to load the page for the step.
            step_elements (dict): A dictionary containing information about elements on the page.
            check_element_present_result (dict): A dictionary containing the results of element checks.
            element_detail_msg (str): A message template for element visibility.

        Returns:
            tuple: A tuple containing the comic out file content as a dictionary and any step errors as a string.

        Example:
            step_name = "Step 1"
            step_image = "step1.png"
            step_page_load_time = "3.45 seconds"
            step_elements = {
                'e1': {'id': 'msg_info', 'type': 'h1', 'text': 'Welcome to Rasree App'},
                'e2': {'id': 'log_info', 'type': 'h1', 'text': 'No One is currently Logged in'}
            }
            check_element_present_result = {
                'e1': {'found': True},
                'e2': {'found': False}
            }
            element_detail_msg = "An element with ID {}, type {}, and text {} is present."
            comic_content, errors = write_comic_out_content(step_name, step_image, step_page_load_time, 
                                   current_page_elements, check_element_present_result, 
                                   element_detail_msg) 
        
        Output Example :
            (
                {
                'step_name': 'Step 1', 
                'image': 'step1.png', 
                'render_time': '3.45 seconds', 
                'e1_details': 'An element with ID msg_info, 
                              type h1, and text Welcome to Rasree App is present.',
                'e1_result': True, 
                'e2_details': 'An element with ID log_info, type h1, and 
                             text No One is currently Logged in is present.', 
                'e2_result': False
               },
            ''
          )
        '''
        
        step_error= ""
        element_check_readable_response_step_error_dict= {}
        current_page_elements = step_input_data_dict["elements_to_be_tested"]
        element_detail_msg = step_input_data_dict["element_detail_msg"]

        try:
            element_check_readable_response_dict={}
            element_check_readable_response_dict['Step']= step_input_data_dict["step_name"]
            element_check_readable_response_dict['Details']= step_input_data_dict["step_desciption"]
            element_check_readable_response_dict['Screenshots'] = step_input_data_dict["screenshot_name"]
            element_check_readable_response_dict['Time_taken']= step_02_page_load_time
            
            for element_key in current_page_elements:
                element_check_readable_response_dict[element_key+'_details'] = element_detail_msg.format(current_page_elements[element_key]['id'], current_page_elements[element_key]['type'], current_page_elements[element_key]['text'])
                element_check_readable_response_dict[element_key+'_result'] = step_02_check_element_present_result[element_key]['found']
        
        except Exception as e:
                step_error+=f"FATAL: Unhandled exception stoping step execution: {e}\n"
                traceback.print_exc()
                element_check_readable_response_step_error_dict["element_check_readable_response_function"] = step_error
        
        return element_check_readable_response_dict , element_check_readable_response_step_error_dict



    def write_comic_out_yaml(self, comic_out_file_name: str, comic_out_content: dict):

        '''
        Write the test output data into a YAML file.

        Args:
            filename (str): The name of the file where the output will be stored.
            out_content (dict): The content of the file in dictionary format.

        Note:
            The function will append to the existing file or create a new file if it doesn't exist.

        Example:
            comic_out_content = {
                'date_time': '2023-08-03-10-30-45',
                'step1': {'found': True, 'duration': 2.35},
                'step2': {'found': False, 'duration': 0.78},
                # ...
            }
            write_comic_out('comic_out.yaml', comic_out_content)
        '''
        # Define the path where you want to save the YAML file

        title = "Unsigned Home Page"
        output_directory = "./Reports"
        comic_out_directory = os.path.join(output_directory, title)

        if not os.path.exists(comic_out_directory):
            os.makedirs(comic_out_directory)

        comic_out_directory_path =  os.path.join(comic_out_directory, "comic_output.yaml")

        with open(str(comic_out_directory_path), 'a+') as file:
            yaml.dump(comic_out_content, file, default_flow_style=False)


    def inputExploreBtn(self,step_data_input:Dict[str,Any]):
        """
        Clicks on the 'inputExploreBtn' element on the page, measures the time before and after,
        verifies the page title, and takes screenshots before and after the click operation.

        Returns:
            dict: A dictionary containing six keys:
                - "step" (str): The step number or description of the action.
                - "testing_function" (str): The name of the testing function being executed.
                - "details" (str): Contains either an error message or a message confirming the page title match.
                - "result" (bool): True if the page title matches the expected title, False otherwise.
                - "time_taken" (float): The time taken in seconds between clicking the element and checking the conditions.
                - "screenshots" (list): A list containing the paths to the screenshots taken before and after the click operation.
        """

        element_to_click = step_data_input["element_to_click"]
            # Define the expected title
        expected_title = step_data_input["expected_title"]
        Step  =  step_data_input["step_name"]
        Testing_function =  step_data_input["step_description"]


        # Record the start time before clicking the element
        start_time = time.time()

        # Capture a screenshot before clicking the element
        step_name = "Before_Click"
        screenshot_before = self.capture_screenshot(step_name,element_to_click)

        # Click on the 'inputExploreBtn' element
        self.driver.find_element(By.ID, element_to_click).click()

        # Capture a screenshot after clicking the element
        step_name = "After_Click"
        screenshot_after = self.capture_screenshot(step_name,element_to_click)

        # Record the end time after checking conditions and getting the actual title
        end_time = time.time()

        # Calculate the time taken for the click operation and title verification
        time_taken = end_time - start_time

    
        # Get the actual title of the page
        actual_title = self.driver.title

        # Check if the actual title matches the expected title
        if expected_title not in actual_title:
            details = f"Page title '{actual_title}' does not match expected title '{expected_title}'"
            result = False
        else:
            details = f"Page title '{actual_title}' matches expected title '{expected_title}'"
            result = True

        return {
            "Step": Step,
            "Testing_function": Testing_function,
            "Details": details,
            "Result": result,
            "Time_taken": time_taken,
            "Screenshots": [screenshot_before, screenshot_after]
        }


    def capture_screenshot(self, step_name, test_name):
        ''' 
        Captures a screenshot of the current browser window and 
        saves it with the given step_name.

        Input attributes:
            step_name (str): The name of the step for which the screenshot is captured.
            test_name (str): The name of the test to create a directory for storing the screenshots.
        '''

        # Create a directory for storing the screenshots if it doesn't exist
        screenshots_directory = "./screenshot"
        test_directory = os.path.join(screenshots_directory, test_name)

        if not os.path.exists(test_directory):
            os.makedirs(test_directory)

        screenshot_path = os.path.join(test_directory, f"{step_name}.png")
        self.driver.get_screenshot_as_file(screenshot_path)
        return screenshot_path




    def output_comic_content_md(self,element_check_readable_response_dict:dict,result_dictionary_list: list):
        '''
        Generate a Markdown file with the comic output based on the provided result_dictionary_list.

        Input attribute:
            result_dictionary_list (list): A list of dictionaries containing the test results.

        Output:
            Generates a Markdown file named 'comic_output.md' with the comic output content.
        '''

        # Get the current date and time
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Create the title with date and time
        title_with_datetime = f"Unsigned Home Page - {current_datetime}"
        title = "Unsigned Home Page"
        output_directory = "./Reports"
        comic_out_directory = os.path.join(output_directory, title)

        if not os.path.exists(comic_out_directory):
            os.makedirs(comic_out_directory)

        comic_out_directory_path =  os.path.join(comic_out_directory, title_with_datetime)
        

        comic_generated_md_file = MdUtils(file_name=comic_out_directory_path, title=title_with_datetime)

        comic_generated_md_file.new_header(level=2, title=element_check_readable_response_dict["Step"], add_table_of_contents="n")
        comic_generated_md_file.new_header(level=3, title="Details", add_table_of_contents="n")
        comic_generated_md_file.new_list([element_check_readable_response_dict['Details']])
        comic_generated_md_file.new_header(level=3, title="Time_taken", add_table_of_contents="n")
        comic_generated_md_file.new_list([str(element_check_readable_response_dict['Time_taken'])])
        comic_generated_md_file.new_header(level=3, title="Screenshots", add_table_of_contents="n")
        comic_generated_md_file.new_list([str(element_check_readable_response_dict['Screenshots'])])
        comic_generated_md_file.new_header(level=3, title="Elements Details and Results", add_table_of_contents="n")
        

        for key, value in element_check_readable_response_dict.items():
            if key.startswith('element_') and key.endswith('_details'):
                element_number = key.split('_')[1]
                element_result_key = f"element_{element_number}_result"

                if element_result_key in element_check_readable_response_dict:
                    comic_generated_md_file.new_header(level=4, title="Element Details", add_table_of_contents="n")
                    comic_generated_md_file.new_list([str(value)])
                    comic_generated_md_file.new_header(level=4, title="Element Result", add_table_of_contents="n")
                    comic_generated_md_file.new_list([str(element_check_readable_response_dict[element_result_key])])



        for item in result_dictionary_list:
            # Add headers and content to the Markdown file
            comic_generated_md_file.new_header(level=2, title=item["Step"], add_table_of_contents="n")
            comic_generated_md_file.new_header(level=3, title="Testing_function", add_table_of_contents="n")
            comic_generated_md_file.new_list([item['Testing_function']])
            comic_generated_md_file.new_header(level=3, title="Details", add_table_of_contents="n")
            comic_generated_md_file.new_list([item['Details']])
            comic_generated_md_file.new_header(level=3, title="Result", add_table_of_contents="n")
            comic_generated_md_file.new_list([str(item['Result'])])
            comic_generated_md_file.new_header(level=3, title="Time_taken", add_table_of_contents="n")
            comic_generated_md_file.new_list([str(item['Time_taken'])])
            comic_generated_md_file.new_header(level=3, title="Screenshots", add_table_of_contents="n")
            comic_generated_md_file.new_list([str(item['Screenshots'])])

            comic_generated_md_file.new_line()

        comic_generated_md_file.create_md_file()
