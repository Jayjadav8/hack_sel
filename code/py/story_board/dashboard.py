import sys
import yaml
from yaml2object import YAMLObject
from datetime import datetime
from browser_app_steps import BrowserAppSteps

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

        # print_dict = {
        #     "url": str(self.story.step_04_02.url),
        #     "scr_shot_needed": bool(self.story.step_04_02.screenshot_needed),
        #     "wait": str(self.story.step_04_02.wait.type),
        #     "duration": int(self.story.step_04_02.wait.duration),
        #     "page_checks":  page_checks,
        #     "exit_element": exit_element,
        #     "screen_shot_path": self.story.screenshot_path,
        #     "screen_shot_name": self.story.step_04_02.screenshot_name,
        #     "sl_time": self.story.sl_time
        # }

        # # Print the dictionary with variable names and their values
        # for key, value in print_dict.items():
        #     print(f"{key}: {value}")

        comic_out_content_dict ={}
        comic_out_content_dict['date_time']= datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
        url = str(self.story.step_04_02.url)
        scr_shot_needed = bool(self.story.step_04_02.screenshot_needed)
        wait=str(self.story.step_04_02.wait.type)
        duration= int(self.story.step_04_02.wait.duration)
        page_checks= (self.story.step_04_02.check_elements).to_dict()
        exit_element=(self.story.step_04_02.exit_element).to_dict()
        screen_shot_path = self.story.screenshot_path
        screen_shot_name = self.story.step_04_02.screenshot_name
        sl_time= self.story.sl_time
        wait_element_id = "inputHomeIcon"

        step_04_02_check_element_present_result, step_04_02_page_load_time, step_04_02_errors\
                        = self.visit_page(url, wait, duration, scr_shot_needed,\
                         page_checks, exit_element, screen_shot_path, screen_shot_name,wait_element_id) 

        comic_out_file= self.story.comic_out_name
        
        # Creating comic_out yaml file
        self.write_comic_out(comic_out_file, comic_out_content_dict)
        

        current_step_elements= (self.story.step_04_02.check_elements).to_dict()
        element_detail_msg= self.story.element_detail_msg
        step_name= self.story.step_04_02.name
        step_image = self.story.step_04_02.screenshot_name
    
        comic_out_content_dict_04_02, step_error_list = self.write_comic_out_content\
                     (step_name, step_image, step_04_02_page_load_time,\
                    current_step_elements, step_04_02_check_element_present_result,\
                    element_detail_msg)
    
    
        comic_out_content_dict["step_04_02"]= comic_out_content_dict_04_02

        comic_out_path= self.story.comic_out_path
        comic_out_name= self.story.comic_out_name
        comic_out_title= self.story.comic_out_title
        comic_file_name = self.story.comic_file_name

        # Creating comic_out md file
        self.write_comic_file(comic_out_path, comic_out_name,\
                               comic_file_name, comic_out_title, comic_out_content_dict)






        # pass

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
