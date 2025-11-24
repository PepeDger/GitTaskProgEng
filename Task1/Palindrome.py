def is_palindrome(text):
    if not isinstance(text, str):
        raise TypeError("Ввод должен быть стокой")
    cleaned_text = ''.join(text.lower().split())
    return cleaned_text == cleaned_text[::-1]


if __name__ == '__main__':
    print(is_palindrome("kekц"))
