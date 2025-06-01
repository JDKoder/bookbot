def get_word_count(book_contents):
    words_list = book_contents.split()
    return len(words_list)


def char_counts(book_contents):
    char_dict = {}
    for i in range(0, len(book_contents)):
        character = book_contents[i].lower()
        if character in char_dict:
            char_dict[character] = char_dict[character] + 1
        else:
            char_dict[character] = 1
    return char_dict


def sort_char_counts(char_counts_dict):
    dicts = []
    for key in char_counts_dict:
        # Initialize empty dictionary to hold char num key value pair
        char_num_dict = {}
        char_num_dict["char"] = key
        char_num_dict["num"] = char_counts_dict[key]
        dicts.append(char_num_dict)
    dicts.sort(reverse=True, key=sort_dict_on)
    return dicts


def sort_dict_on(char_dict):
    return char_dict["num"]
