def count_words(book_text: str) -> int:
    words = book_text.split()
    return len(words)

def count_chars(book_text: str) -> dict[str, int]:
    char_count = {}
    for char in book_text:
        char = char.lower()
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_chars_count(chars_count: dict[str, int]) -> list[dict[str, str | int]]:
    sorted_chars_count = []
    for char, count in chars_count.items():
        sorted_chars_count.append({'char': char, 'count': count})
    sorted_chars_count.sort(key=lambda x: x['count'], reverse=True)
    return sorted_chars_count