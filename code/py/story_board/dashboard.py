import sys
import yaml
from yaml2object import YAMLObject
from datetime import datetime
from browser_app_steps import BrowserAppSteps
from operational_functions import *

class TestPage01unsignedhomepage(BrowserAppSteps):

    '''
    A class representing the comic story for the unsigned home page.
    '''
    story = {}

    def __init__(self, comic_data):
        '''
        Initializes the TestPage01unsignedhomepage object.
        Args:
            comic_data (YAMLObject): The YAMLObject containing comic story data.
        '''
        super().__init__(browser=comic_data.browser, browser_server_url=comic_data.browser_server_url,
                         duration=comic_data.driver_wait)
        self.story = comic_data

    def test_page01unsignedhomepage(self):
        '''
         Implements the comic story steps for the unsigned home page.
        '''

        # Convert yaml object to dictionary.
        comic_dashboard_data = self.story.to_dict()
        step_04_02_data = self.story.step_04_02.to_dict()
        screen_shot_path = comic_dashboard_data["screenshot_path"]
        step_04_02_data["screen_shot_path"] =screen_shot_path
        sl_time= comic_dashboard_data["sl_time"]
        step_name= step_04_02_data["name"]
        step_image = step_04_02_data["screenshot_name"]        
        element_detail_msg= comic_dashboard_data["element_detail_msg"]
        
        wait_element_id = "inputHomeIcon"

        # Creating comic_out yaml file
        comic_out_content_dict ={}
        comic_out_content_dict['date_time']= datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
        comic_out_file= comic_dashboard_data["comic_out_name"]


        # Check all the elements to be tested are present or not.
        step_04_02_check_element_present_result, step_04_02_page_load_time, step_04_02_errors\
                        = self.visit_page(step_04_02_data,wait_element_id) 

        # generate dictionary for md file content which describes  element present or not.
        current_step_elements= step_04_02_data["check_elements"]
        comic_out_content_dict_04_02 = self.write_comic_out_content\
                     (step_name, step_image, step_04_02_page_load_time,\
                    current_step_elements, step_04_02_check_element_present_result,\
                    element_detail_msg)

        comic_out_content_dict["step_04_02"]= comic_out_content_dict_04_02


        # Checking different elements as per requirements.

        # Step_01_03 : Clicks on the 'inputExploreBtn' element on the page and verifies the page title.
        # comic_out_content_dict["step_01_03"] = inputExploreBtn(self)


    
        # Creating comic_out yaml file
        self.write_comic_out(comic_out_file, comic_out_content_dict)
        


        # Creating comic_out md file 
        comic_out_path= comic_dashboard_data["comic_out_path"]
        comic_out_name= comic_dashboard_data["comic_out_name"]
        comic_out_title= comic_dashboard_data["comic_out_title"]
        comic_file_name = comic_dashboard_data["comic_file_name"]
        self.write_comic_file(comic_out_path, comic_out_name,\
                               comic_file_name, comic_out_title, comic_out_content_dict)



    def __del__(self):
        if self.driver is not None:
            self.driver.quit()


if __name__ == '__main__':
    n = len(sys.argv)
    if n != 2:
        print("Usage: python dashboard.py <config_file>")
        sys.exit(1)

    config_file = sys.argv[1]
    try:
        with open("./" + config_file, "r") as f:
            comic_data = yaml.safe_load(f)
        dashboard_config = YAMLObject('comic_in', (object,),\
             {'source': comic_data, 'namespace': 'comic_dashboard_data'})

        dashboard = TestPage01unsignedhomepage(dashboard_config)
        dashboard.test_page01unsignedhomepage()

    except FileNotFoundError:
        print("ERROR: comic.yaml file not found.")
        sys.exit(1)
