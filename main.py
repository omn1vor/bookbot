with open("books/frankenstein.txt") as f:
    text = f.read()
    words_count = len(text.split())
    print(words_count)