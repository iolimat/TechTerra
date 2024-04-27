def all_words_under_100_char(my_list):
    return all(len(word) <= 100 for word in my_list)

def the_number_of_words(my_list):
    return len(my_list) > 20

def count_of_special_and_numbers(paragraph):
    max_count = len(paragraph) * 0.3
    special_symbols = "!@#$%^&*()[]{};:'\"\\|"
    count = 0
    for char in paragraph:
        if char in special_symbols or char.isdigit():
            count += 1
    return count <= max_count

def check_the_document(my_list):
    if all_words_under_100_char(my_list) and the_number_of_words(my_list.strip().split()):
        paragraph = my_list.strip()
        if count_of_special_and_numbers(paragraph):
            ######### make the cleaning step here please
            return paragraph

    return ""
