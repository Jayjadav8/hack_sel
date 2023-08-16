import sys
import yaml
from yaml2object import YAMLObject
from datetime import datetime
from browser_app_steps import BrowserAppSteps
import os

class TestPage(BrowserAppSteps):
    '''
    A class representing the comic story for the unsigned home page.
    '''
    story = {}

    def __init__(self, comic_data):

        '''
        Initializes the TestPage object.
        Args:
            comic_data (YAMLObject): The YAMLObject containing comic story data.

        '''
        super().__init__(browser=comic_data.step_01_01.browser, browser_server_url=comic_data.step_01_01.browser_server_url)
        self.story = comic_data

    def test_page(self):
        '''
         Implements the comic story steps for the Test page.
        '''
     
        # Convert yaml object to dictionary.
        comic_dashboard_general_data_dict = self.story.to_dict()
        comic_out_element_functionality_test_list_response = []
        comic_out_content_dict ={}
        

        for step_name, step_data in comic_dashboard_general_data_dict.items():
            step_functionality = step_data.get('step_functionality')

            if step_functionality == 'general_info':
                pass

            elif step_functionality == 'validate_element':

                # Check all the elements to be tested on step 2 listed are present or not.
                check_element_present_result, page_load_time, error_exist_dict\
                                = self.visit_page_to_be_tested_in_step(step_data) 
                
                if bool(error_exist_dict):
                    print("The dictionary is not empty.")
                    # TODO : abort testing and generate report.

                # Generating readable response of element presences in step 2 listed,
                # which would be input to function which generate md readable file.
                element_check_readable_response_dict , readable_error_dict = \
                    self.element_check_readable_response(step_data,\
                        check_element_present_result , page_load_time)
                
                key_name = step_data.get('step_name')

                comic_out_content_dict[f"{key_name}"]= element_check_readable_response_dict
                
                if bool(readable_error_dict):
                    print("The dictionary is not empty.")
                # TODO : abort testing and generate report.

   
            elif step_functionality == 'clickability':

                # Checking functionality of clickability element:
                comic_out_clicability_content_dict = self.clickabilityCheck(step_data)
                
                key_name = step_data.get('step_name')
                comic_out_content_dict[f"{key_name}"]= comic_out_clicability_content_dict

                # Generating md readable file : comic_output.md
                comic_out_element_functionality_test_list_response.append(comic_out_clicability_content_dict)

            elif step_functionality == 'send_keys':

                # Checking functionality of clickability element:
                comic_out_clicability_content_dict = self.check_element_interaction(step_data)
                
                key_name = step_data.get('step_name')
                comic_out_content_dict[f"{key_name}"]= comic_out_clicability_content_dict

                # Generating md readable file : comic_output.md
                comic_out_element_functionality_test_list_response.append(comic_out_clicability_content_dict)


            else:
                # Handle other cases or provide a default action
                pass


        

        
        # comic_out_file_name= comic_dashboard_general_data_dict["comic_out_name"]
        comic_out_file_name = "comic_output.yaml"  
        self.write_comic_out_yaml(comic_out_file_name, comic_out_content_dict)

        self.output_comic_content_md(element_check_readable_response_dict,\
                                  comic_out_element_functionality_test_list_response)


    def __del__(self):
        if self.driver is not None:
            self.driver.quit()


if __name__ == '__main__':
    
    command_line_input_length = len(sys.argv)
    if command_line_input_length != 2:
        print("Usage: python dashboard.py <config_file>")
        sys.exit(1)

    config_file = sys.argv[1]
   
    try:
        config_directory = "test_data"

        # Construct the full path to the configuration file
        config_file_path = os.path.join(config_directory, config_file)

        # Load the YAML content from the file
        with open(config_file_path, "r") as f:
            comic_data = yaml.safe_load(f)

        test_page_input_config = YAMLObject('comic_in', (object,),\
             {'source': comic_data, 'namespace': 'comic_in'})

        test_page_object = TestPage(test_page_input_config)
        test_page_object.test_page()

    except FileNotFoundError:
        print("ERROR: comic.yaml file not found.")
        sys.exit(1)
