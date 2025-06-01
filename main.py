from stats import get_word_count
from stats import char_counts
from stats import sort_char_counts
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def print_report(book_path, word_count, sorted_char_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_num_dict in sorted_char_counts:
        if char_num_dict["char"].isalpha():
            character = char_num_dict["char"]
            num_occurrences = char_num_dict["num"]
            print(f"{character}: {num_occurrences}")
    print("============= END ===============")


def main():
    # check sys.argv for 2 argumens: 0: file to run, 1: relative path to book
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    ccounts = char_counts(book_text)
    # print(f"{ccounts}")
    # print(f"{word_count} words found in the document")
    sorted_counts = sort_char_counts(ccounts)
    # print(f"{word_count}{sorted_counts}")
    print_report(book_path, word_count, sorted_counts)


main()
