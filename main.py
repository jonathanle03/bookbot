import sys
from stats import get_num_words
from stats import get_num_chars
from stats import sort_dict

def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)

    num_words = get_num_words(file_contents)
    num_chars = get_num_chars(file_contents)
    list_of_chars = sort_dict(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in list_of_chars:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    
    print("============= END ===============")

main()