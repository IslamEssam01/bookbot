def get_word_count(text: str) -> int:
    return len(text.split())


def get_char_count(text: str) -> dict[str, int]:
    text = text.lower()
    count: dict[str, int] = {}

    for char in text:
        if char.isspace():
            continue

        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    return count


def get_sorted_counts(char_count: dict[str, int]) -> list[dict]:
    counts: list[dict] = list(
        map(lambda char: {"char": char, "count": char_count[char]}, char_count)
    )

    counts.sort(reverse=True, key=lambda count: count["count"])
    return counts
