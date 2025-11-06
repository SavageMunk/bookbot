def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    chars = {}
    for a in text.lower():
        if a in chars:
            chars[a] += 1
        else:
            chars[a] = 1
    return chars

def sort_on(item):
    return item["num"]

def chars_dict_to_sorted_list(char_dict):
    char_list = []
    for char, num in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    