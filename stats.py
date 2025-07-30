def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_num_chars(text):
    num_chars = {}
    for char in text:
        char = char.lower()
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars

def sort_on(items):
    return items["num"]

def sort_dict(data):
    list_of_dict = []
    for char in data:
        list_of_dict.append({"char": char, "num": data[char]})
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict