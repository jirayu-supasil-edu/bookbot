from stats import get_num_words, get_char_dict, get_char_dict_list
import sys

def get_book_text(filepath:str)->str:
    '''
    Open file and return contents
    '''
    with open(file = filepath) as f:
        
        book_text = f.read()

    return book_text

def main():
    argv_list = sys.argv
    if len(argv_list) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = f"./{argv_list[1]}"
    book_text = get_book_text(filepath = book_path)
    num_words = get_num_words(text= book_text)
    char_dict = get_char_dict(text=book_text)
    char_dict_list = get_char_dict_list(char_dict= char_dict)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path[1:]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_dict_list:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")




main()
    

