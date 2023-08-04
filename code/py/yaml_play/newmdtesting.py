from mdutils import MdUtils

def create():
    result_dictionary_list = []

    new_dict1 = {
        "step": "step 3",
        "testing_function": "xyz",
        "details": "abc",
        "result": True
    }

    new_dict2 = {
        "step": "step 4",
        "testing_function": "mno",
        "details": "abc1",
        "result": False
    }

    result_dictionary_list.append(new_dict1)
    result_dictionary_list.append(new_dict2)

    comic_generated_md_file = MdUtils(file_name='result_file', title='Result Dictionary List')

    for item in result_dictionary_list:
        # print(item)
        comic_generated_md_file.new_header(level=2, title=item['step'], add_table_of_contents="n")
        comic_generated_md_file.new_header(level=3, title="testing_function", add_table_of_contents="n")
        comic_generated_md_file.new_list([item['testing_function']])
        comic_generated_md_file.new_header(level=3, title="details",add_table_of_contents="n")
        comic_generated_md_file.new_list([item['details']])
        comic_generated_md_file.new_header(level=3, title="result",add_table_of_contents="n")
        comic_generated_md_file.new_list([str(item['result'])])
        comic_generated_md_file.new_line()

    comic_generated_md_file.create_md_file()

create()