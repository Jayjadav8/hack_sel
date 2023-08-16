import sys
import yaml
from yaml2object import YAMLObject
from datetime import datetime
from browser_app_steps import BrowserAppSteps


class TestPage01UnsignedHomePage(BrowserAppSteps):
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
        super().__init__(browser=comic_data.step_01_01.browser, browser_server_url=comic_data.step_01_01.browser_server_url)
        self.story = comic_data

    def test_page_01_unsigned_home_page(self):
        '''
         Implements the comic story steps for the unsigned home page.
        '''
            # Convert yaml object to dictionary.
        comic_dashboard_general_data_dict = self.story.to_dict()
        step_02_data_dict = self.story.step_01_02.to_dict()
        step_02_element_check_readable_response_dict = {}
        comic_out_explore_button_content_dict = {}

        for step_name, step_data in comic_dashboard_general_data_dict.items():
            step_functionality = step_data.get('step_functionality')

            if step_functionality == 'general_info':
                print(step_data.get('step_name'))
                # Do something for the "general_info" step_functionality

            elif step_functionality == 'validate_element':
                print(step_data.get('step_name'))

                # Check all the elements to be tested on step 2 listed are present or not.
                step_02_check_element_present_result, step_02_page_load_time, step_02_error_dict\
                                = self.visit_page_to_be_tested_in_step(step_02_data_dict) 
                
                if bool(step_02_error_dict):
                    print("The dictionary is not empty.")
                    # TODO : abort testing and generate report.

                # Generating readable response of element presences in step 2 listed,
                # which would be input to function which generate md readable file.
            
                step_02_element_check_readable_response_dict , step_02_readable_error_dict = \
                    self.element_check_readable_response(step_02_data_dict,\
                        step_02_check_element_present_result , step_02_page_load_time)
                
                if bool(step_02_readable_error_dict):
                    print("The dictionary is not empty.")
                # TODO : abort testing and generate report.

   
            elif step_functionality == 'clickability':
                # Do something for the "clickability" step_functionality
                print(step_data.get('step_name'))

                step_03_data_dict = self.story.step_01_03.to_dict()

                    # Checking functionality of clickability element:
                comic_out_explore_button_content_dict = self.inputExploreBtn(step_03_data_dict)



            else:
                # Handle other cases or provide a default action
                pass




        # Creating comic_out yaml file
        comic_out_content_dict ={}
        comic_out_content_dict["visitStep"]= step_02_element_check_readable_response_dict
        comic_out_content_dict["Explore"]= comic_out_explore_button_content_dict
        
        # comic_out_file_name= comic_dashboard_general_data_dict["comic_out_name"]
        comic_out_file_name = "comic_output.yaml"  
        self.write_comic_out_yaml(comic_out_file_name, comic_out_content_dict)


        # Generating md readable file : comic_output.md
        comic_out_element_functionality_test_list_response = []
        comic_out_element_functionality_test_list_response.append(comic_out_explore_button_content_dict)
        self.output_comic_content_md(step_02_element_check_readable_response_dict,\
                                  comic_out_element_functionality_test_list_response)


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
        unsigned_home_page_config = YAMLObject('comic_in', (object,),\
             {'source': comic_data, 'namespace': 'comic_in'})

        test_unsigned_home_page_object = TestPage01UnsignedHomePage(unsigned_home_page_config)
        test_unsigned_home_page_object.test_page_01_unsigned_home_page()

    except FileNotFoundError:
        print("ERROR: comic.yaml file not found.")
        sys.exit(1)