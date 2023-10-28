def main():
    text = read_file()
    words_count = len(text.split())
    letters = {}
    for letter in text.lower():
        letters[letter] = letters.get(letter, 0) + 1
    sorted_letters = get_sorted_letters(letters)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document")
    print()
    for item in sorted_letters:
        print(f"The '{item['char']}' character was found {item['count']} times")    
    
def read_file():
    with open("books/frankenstein.txt") as f:
        return f.read()

def get_sorted_letters(letters):
    sorted_list = []
    for k, v in letters.items():
        if not k.isalpha():
            continue
        sorted_list.append({"char": k, "count": v})

    sorted_list.sort(key=lambda i: i["count"], reverse=True)
    return sorted_list

main()