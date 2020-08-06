def no_dups(s):
    prevWords = set(())
    words = s.split(" ")
    no_duplicates_string = ""

    for w in words:
        if w not in prevWords:
            no_duplicates_string += f"{w} "

        prevWords.add(w)

    return str.strip(no_duplicates_string)


if __name__ == "__main__":
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
