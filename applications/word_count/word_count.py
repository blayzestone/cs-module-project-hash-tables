def word_count(s):
    ignored_chars = (
        '"',
        ":",
        ";",
        ",",
        ".",
        "-",
        "+",
        "=",
        "/",
        "\\",
        "|",
        "[",
        "]",
        "{",
        "}",
        "(",
        ")",
        "*",
        "^",
        "&",
    )
    word_counts = {}
    formattedString = ""

    for char in s:
        if char not in ignored_chars:
            formattedString += char

    formattedString = formattedString.split()

    for word in formattedString:
        if word:
            word = word.lower()
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    return word_counts


if __name__ == "__main__":
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(
        word_count(
            "This is a test of the emergency broadcast network. This is only a test."
        )
    )

