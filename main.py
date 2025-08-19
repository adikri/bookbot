import sys

if(len(sys.argv) != 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

from stats import num_of_words
from stats import num_of_chars
from stats import sort_char_dict

def main():
    # print(get_book_text("./books/frankenstein.txt"))
    content = get_book_text(filepath)
    # print(content)
    word_count = num_of_words(content)
    # print(f"{word_count} words found in the document")

    char_count_dict = num_of_chars(content)
    # print(char_count_dict)

    sorted_char_list = sort_char_dict(char_count_dict) 

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_list:
        char = item["char"]
        count = item["num"]
        print(f"{char}: {count}")
    print("============= END ===============")
    

main()