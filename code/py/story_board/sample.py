
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
import yaml
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta
from mdutils.mdutils import MdUtils



# def sample():
#     step_name = "Step 1"
#     step_image = "step1.png"
#     step_page_load_time = "3.45 seconds"
#     current_page_elements = {
#         'e1': {'id': 'msg_info', 'type': 'h1', 'text': 'Welcome to Rasree App'},
#         'e2': {'id': 'log_info', 'type': 'h1', 'text': 'No One is currently Logged in'}
#     }
#     check_element_present_result = {
#         'e1': {'found': True},
#         'e2': {'found': False}
#     }
#     element_detail_msg = "An element with ID {}, type {}, and text {} is present."

#     step_error= ""
#     step_error_list=""
#     try:
#         cout={}
#         cout['step_name']= step_name
#         cout['image'] = step_image
#         cout['render_time']= step_page_load_time

#         for element_key in current_page_elements:
#             cout[element_key+'_details'] = element_detail_msg.format\
#                                         (current_page_elements[element_key]['id'],\
#                                         current_page_elements[element_key]['type'],\
#                                         current_page_elements[element_key]['text'])
            
#             cout[element_key+'_result'] = check_element_present_result[element_key]['found']

#     except Exception as e:
#             step_error+=f"FATAL: Unhandled exception stoping step execution: {e}\n"
#             # traceback.print_exc()
#     step_error_list+= step_error
#     return cout, step_error_list


# print(sample())


def write_comic_file():
    
    '''
    Write the comic file based on the provided comic_out_content_dict.

    Args:
        comic_out_path (str): The path where the comic output YAML file should be stored.
        comic_out_name (str): The filename for the comic output in YAML format.
        comic_file_name (str): The filename for the comic output in Markdown format.
        comic_out_title (str): The title of the comic story.
        comic_out_content_dict (dict): A dictionary containing the content of the comic steps.

    Returns:
        str: Any step errors encountered during writing the comic file.

    Example:
        comic_out_path = "./"
        comic_out_name = "comic_out.yaml"
        comic_file_name = "comic_out.md"
        comic_out_title = "unsigned home Page story"
        comic_out_content_dict = {
            'Step 1': {
                'image': 'step1.png',
                'render_time': '3.45 seconds',
                'e1_details': 'An element with ID msg_info, type h1, and text Welcome to Rasree App is present.',
                'e1_result': True,
                'e2_details': 'An element with ID log_info, type h1, and text No One is currently Logged in is present.',
                'e2_result': False
            },
            'Step 2': {
                # Other step details
            },
            # More steps...
        }
        step_errors = write_comic_file(comic_out_path, comic_out_name, comic_file_name, 
                                    comic_out_title, comic_out_content_dict)
    '''

    comic_out_path = "./"
    comic_out_name = "comic_out.yaml"
    comic_file_name = "comic_out.md"
    comic_out_title = "unsigned home Page story"
    comic_out_content_dict = {
        'Step 1': {
            'image': 'step1.png',
            'render_time': '3.45 seconds',
            'e1_details': 'An element with ID msg_info, type h1, and text Welcome to Rasree App is present.',
            'e1_result': True,
            'e2_details': 'An element with ID log_info, type h1, and text No One is currently Logged in is present.',
            'e2_result': False
        },
        'Step 2': {
            # Other step details
        }
        # More steps...
    }


    step_error = ""
    step_error_list = ""
    file_name= comic_out_path+ comic_file_name

    try:
    
        current_time = (datetime.now(tz=ZoneInfo('Asia/Kolkata'))).strftime('%H:%M:%S')


        comic_generated_md_file = MdUtils(file_name)
        comic_generated_md_file.new_header(level=1, title=f' {comic_out_title} {current_time}')

        for comic_step in comic_out_content_dict:

            if comic_step != "date_time":
                comic_generated_md_file.new_line()
                comic_generated_md_file.new_header(level=2, title= f' {comic_step} : ')

                for check in comic_out_content_dict[comic_step]:

                    if check == "image":
                        comic_generated_md_file.new_line()
                        comic_generated_md_file.new_header(level=3, title= "Screenshot: ")
                        comic_generated_md_file.new_line(comic_generated_md_file.new_inline_image(text= "", path=f"./comic/{comic_out_content_dict[comic_step][check]}"))
                    comic_generated_md_file.new_line()
                    comic_generated_md_file.new_line(f"{check}: {comic_out_content_dict[comic_step][check]}")
                    
        comic_generated_md_file.create_md_file()
    
    except FileNotFoundError as e:
        step_error=f"No File named {e} found\n"
        print("step error: ",step_error)
    
    except Exception as e:
        step_error="FATAL: In click element to load page, Unhandled Exception, see printed log\n"
        print("step error: ",step_error)

    step_error_list+= step_error
    return step_error_list

write_comic_file()