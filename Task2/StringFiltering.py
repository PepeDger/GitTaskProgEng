from typing import List, Callable


def filter_strings(filter_func: Callable[[str], bool], string_array: List[str]):
    return [s for s in string_array if filter_func(s)]


if __name__ == '__main__':
    strings = ["apple", "banana", "a test",
               "hello world", "cat", "dog", "elephant"]

    no_spaces = filter_strings(lambda s: ' ' not in s, strings)
    print("Без пробелов:", no_spaces)

    no_a_start = filter_strings(lambda s: not s.startswith('a'), strings)
    print("Не начинаются с 'a':", no_a_start)

    length_5_plus = filter_strings(lambda s: len(s) >= 5, strings)
    print("Длина >= 5:", length_5_plus)
