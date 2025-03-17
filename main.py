import sys
from stats import get_word_count, get_char_count, get_sorted_counts


def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()


def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = args[1]
    text = get_book_text(filepath)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    sorted_counts = get_sorted_counts(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for count in sorted_counts:
        if not count["char"].isalpha():
            continue
        print(f"{count["char"]}: {count["count"]}")
    print("============= END ===============")


main()
