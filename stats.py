from operator import itemgetter

def get_num_words(text:str)-> int:
    '''
    Count words from text, return int of word counts
    '''
    list_words = text.split()
    num_words = len(list_words)
    return num_words

def get_char_dict(text:str) -> dict:
    '''
    Return raw dictionary of key-value as character and character counts
    '''
    text = text.lower()
    char_dict = {}
    for char in text:
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1
    return char_dict



def get_char_dict_list(char_dict:dict)->list:
    dict_list = []
    for char in char_dict:
        single_dict = {
            "char": char,
            "num" : char_dict[char]
        }
        dict_list.append(single_dict)

    dict_list.sort(reverse= True, key= itemgetter("num"))

    return dict_list

