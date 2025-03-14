from stats import get_book_words_num
from stats import character_count
from stats import generate_report
import sys

def main():
    if len(sys.argv) < 2:
        print("Error ==> Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    nums, word_count = get_book_words_num(sys.argv[1])
    cnt = character_count(nums)
    generate_report(cnt, word_count)
if __name__ == "__main__":
    main()
