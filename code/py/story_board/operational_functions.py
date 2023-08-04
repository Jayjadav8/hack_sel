from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from mdutils import MdUtils
# ... Other code ...

def inputExploreBtn(self):
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

    # Record the start time before clicking the element
    start_time = time.time()

    # Capture a screenshot before clicking the element
    step_name = "Before_Click"
    screenshot_before = capture_screenshot(self,step_name,"inputExploreBtn")

    # Click on the 'inputExploreBtn' element
    self.driver.find_element(By.ID, "inputExploreBtn").click()

    # Capture a screenshot after clicking the element
    step_name = "After_Click"
    screenshot_after = capture_screenshot(self,step_name,"inputExploreBtn")

    # Record the end time after checking conditions and getting the actual title
    end_time = time.time()

    # Calculate the time taken for the click operation and title verification
    time_taken = end_time - start_time

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

    return {
        "Step": "Step 1",  # Replace this with the appropriate step number or description
        "Testing_function": "inputExploreBtn",
        "Details": details,
        "Result": result,
        "Time_taken": time_taken,
        "Screenshots": [screenshot_before, screenshot_after]
    }

# Function for capturing screenshots
def capture_screenshot(self, step_name, test_name):
    ''' 
    Captures a screenshot of the current browser window and 
    saves it with the given step_name.

    Input attributes:
        step_name (str): The name of the step for which the screenshot is captured.
        test_name (str): The name of the test to create a directory for storing the screenshots.
    '''

    filename = os.path.basename(__file__)

    # Create a directory for storing the screenshots if it doesn't exist
    screenshots_directory = "../screenshot"
    test_directory = os.path.join(screenshots_directory, test_name)
    if not os.path.exists(test_directory):
        os.makedirs(test_directory)
    screenshot_path = os.path.join(test_directory, f"{step_name}.png")
    self.driver.get_screenshot_as_file(screenshot_path)
    return screenshot_path


def output_comic_content(result_dictionary_list: list):
    '''
    Generate a Markdown file with the comic output based on the provided result_dictionary_list.

    Input attribute:
        result_dictionary_list (list): A list of dictionaries containing the test results.

    Output:
        Generates a Markdown file named 'comic_output.md' with the comic output content.
    '''

    comic_generated_md_file = MdUtils(file_name='comic_output', title='Unsigned Home Page')

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
