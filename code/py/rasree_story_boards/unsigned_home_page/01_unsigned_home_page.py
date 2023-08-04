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
        super().__init__(browser=comic_data.browser, browser_server_url=comic_data.browser_server_url,
                         duration=comic_data.driver_wait)
        self.story = comic_data

    def test_page_01_unsigned_home_page(self):
        '''
         Implements the comic story steps for the unsigned home page.
        '''

        # Convert yaml object to dictionary.
        comic_dashboard_data = self.story.to_dict()
        step_01_data = self.story.step_04_02.to_dict()

        screen_shot_path = comic_dashboard_data["screenshot_path"]
        
        step_01_data["screen_shot_path"] =screen_shot_path
        
        sl_time= comic_dashboard_data["sl_time"]
        step_name= step_01_data["name"]
        step_image = step_01_data["screenshot_name"]        
        element_detail_msg= comic_dashboard_data["element_detail_msg"]



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

        test_unsigned_home_page_object = TestPage01UnsignedHomePage(dashboard_config)
        test_unsigned_home_page_object.test_page_01_unsigned_home_page()

    except FileNotFoundError:
        print("ERROR: comic.yaml file not found.")
        sys.exit(1)
