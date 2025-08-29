import sys

from stats import count_words, count_chars, sort_chars_count

def get_book_text(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count = count_words(book_text)
    chars_count = count_chars(''.join(book_text.split())) # Remove whitespaces for char count
    sorted_chars_count = sort_chars_count(chars_count)

    report = []
    report.append("============ BOOKBOT ============")
    report.append(f"Analyzing book found at {file_path}...")
    report.append("----------- Word Count ----------")
    report.append(f"Found {word_count} total words")
    report.append("--------- Character Count -------")
    for entry in sorted_chars_count:
        if entry["char"].isalpha(): # type: ignore
            report.append(f"{entry['char']}: {entry['count']}")
    report.append("============= END ===============")
    print('\n'.join(report))


if __name__ == "__main__":
    main()