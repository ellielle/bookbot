def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = count_words(file_contents)
        letters = count_letters(words)
        generate_report(words, letters)


def count_words(file_contents):
    return file_contents.split()


def count_letters(words):
    letter_dict = {}
    for word in words:
        for letter in word:
            if letter.lower() in letter_dict:
                letter_dict[letter.lower()] += 1
            else:
                letter_dict[letter.lower()] = 1

    return letter_dict


def generate_report(words, letters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document\n")

    letter_list = []

    for k, v in letters.items():
        if k.isalpha():
            letter_list.append([k, v])

    letter_list.sort(key=lambda x: x[1], reverse=True)

    for k, v in letter_list:
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")


main()
