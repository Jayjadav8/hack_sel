import yaml
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta
from mdutils.mdutils import MdUtils

def write_comic_file():
    
    step_error = ""
    step_error_list = ""

    comic_out_path = "./"
    # comic_out_name = "comic_out.yaml"
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

    result_dictionary_list = []

    new_dict1 = {
        "step" : "step 3",
        "testing_function" :"xyz",
        "details" : "abc",
        "result": True
    }


    new_dict2 = {
        "step" : "step 4",
        "testing_function" :"mno",
        "details" : "abc1",
        "result": False
    }

    result_dictionary_list.append(new_dict1)
    result_dictionary_list.append(new_dict2)

    file_name= comic_out_path+ comic_file_name

    try:
    
        current_time = (datetime.now(tz=ZoneInfo('Asia/Kolkata'))).strftime('%H:%M:%S')

        # creation of md file
        comic_generated_md_file = MdUtils(file_name)
        
        # Title at H1 level.
        comic_generated_md_file.new_header(level=1, title=f' {comic_out_title} {current_time}')

        # Iterate over input Dictionary
        for comic_step in comic_out_content_dict:
            
            comic_generated_md_file.new_line()
            # Adding step no. at H2 level.
            comic_generated_md_file.new_header(level=2,\
                                     title= f' {comic_step} : ')

            for dict_key in comic_out_content_dict[comic_step]:
                print(dict_key)
                if dict_key == "image":
                    comic_generated_md_file.new_line()
                    comic_generated_md_file.new_header(level=3, title= "Screenshot: ")
                    comic_generated_md_file.new_line(comic_generated_md_file.new_inline_image(text= "", path=f"./comic/{comic_out_content_dict[comic_step][dict_key]}"))
                comic_generated_md_file.new_line()
                comic_generated_md_file.new_line(f"{dict_key}: {comic_out_content_dict[comic_step][dict_key]}")
        

        for dict_steps in result_dictionary_list:


        for comic_step in new_dict:

            comic_generated_md_file.new_line()
                # Adding step no. at H2 level.
            comic_generated_md_file.new_header(level=2,\
                                        title= f' {comic_step["step"]} : ')
            

        
        
        
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