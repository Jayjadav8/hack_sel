# Assuming you have the dictionary named 'element_check_readable_response_dict'
from datetime import datetime
# from mdutils import MdUtils
from mdutils import MdUtils
        # Get the current date and time
current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Create the title with date and time
title_with_datetime = f"Unsigned Home Page - {current_datetime}"
# Define the dictionary
element_check_readable_response_dict = {
    'Step': 'Step 2 ',
    'Details': 'Verify all test elements id are present on page.',
    'Screenshots': '01_01.png',
    'Time_taken': 1.501,
    'element_1_details': 'an element with id inputExploreBtn of type button with text Explore ',
    'element_1_result': True,
    'element_2_details': 'an element with id inputHomeIcon of type img with text \thttps://qbrow.rasree.com/img/rasree-logo.690c3e83.png ',
    'element_2_result': True,
    'element_3_details': 'an element with id inputSearchBar of type type with text Search for subjects, concepts, tutors, etc. ',
    'element_3_result': True,
    'element_4_details': 'an element with id inputViewAllCoursesButton of type button with text View more ',
    'element_4_result': True,
    'element_5_details': 'an element with id inputViewCourseDetails_1 of type button with text View details ',
    'element_5_result': True,
    'element_6_details': 'an element with id inputViewTeamDetailsButton of type button with text View more ',
    'element_6_result': True,
    'element_7_details': 'an element with id inputSignInButton of type button with text Sign in ',
    'element_7_result': True,
}
comic_generated_md_file = MdUtils(file_name='comic_output', title=title_with_datetime)

# comic_generated_md_file = MdUtils(file_name='comic_output', title=title_with_datetime)
# comic_generated_md_file.new_header(level=2, title=element_check_readable_response_dict["Step"], add_table_of_contents="n")
# comic_generated_md_file.new_header(level=3, title="Details", add_table_of_contents="n")
# comic_generated_md_file.new_list([element_check_readable_response_dict['Details']])
# comic_generated_md_file.new_header(level=3, title="Time_taken", add_table_of_contents="n")
# comic_generated_md_file.new_list([str(element_check_readable_response_dict['Time_taken'])])
# comic_generated_md_file.new_header(level=3, title="Screenshots", add_table_of_contents="n")
# comic_generated_md_file.new_list([str(element_check_readable_response_dict['Screenshots'])])

table_data = [["Sr_no.", "Element_name", "Details", "Result"]]
for i in range(1, 8):
    element_details_key = f"element_{i}_details"
    element_result_key = f"element_{i}_result"
    if element_details_key in element_check_readable_response_dict and element_result_key in element_check_readable_response_dict:
        details = element_check_readable_response_dict[element_details_key]
        result = "Passed" if element_check_readable_response_dict[element_result_key] else "Failed"
        table_data.append([i, element_details_key, details, result])

print(table_data)
comic_generated_md_file.new_table(columns=4, rows=len(table_data), text=table_data, text_align='center')

# Save the Markdown file
comic_generated_md_file.create_md_file()