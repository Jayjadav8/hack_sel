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

        comic_out ={}
        comic_out['date_time']= datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
        url = str(self.story.step_04_02.url)
        scr_shot_needed = bool(self.story.step_04_02.screenshot_needed)
        wait=str(self.story.step_04_02.wait.type)
        duration= int(self.story.step_04_02.wait.duration)
        page_checks= self.story.step_04_02.check_elements
        exit_element=self.story.step_04_02.exit_element
        screen_shot_path = self.story.screenshot_path
        screen_shot_name = self.story.step_04_02.screenshot_name
        sl_time= self.story.sl_time

        print_dict = {
            "url": str(self.story.step_04_02.url),
            "scr_shot_needed": bool(self.story.step_04_02.screenshot_needed),
            "wait": str(self.story.step_04_02.wait.type),
            "duration": int(self.story.step_04_02.wait.duration),
            "page_checks": self.story.step_04_02.check_elements,
            "exit_element": self.story.step_04_02.exit_element,
            "screen_shot_path": self.story.screenshot_path,
            "screen_shot_name": self.story.step_04_02.screenshot_name,
            "sl_time": self.story.sl_time
        }

        # Print the dictionary with variable names and their values
        for key, value in print_dict.items():
            print(f"{key}: {value}")




        pass

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
