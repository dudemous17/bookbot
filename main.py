from stats import get_num_words
from stats import get_char_count
from stats import get_sorted
import sys

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file = sys.argv[1]
    file_string = get_book_text(file)
    num_words = get_num_words(file_string)
    char_count = get_char_count(file_string)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_characters = get_sorted(char_count)
    for c in sorted_characters:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")

main()
