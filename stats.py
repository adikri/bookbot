def num_of_words(content):
    word_array = content.split()
    count = 0
    for word in word_array:
        count += 1
    return count

def num_of_chars(content):
    char_dictionary = {}
    for char in content:
        # print(char)
        char = char.lower()
        
        if char in char_dictionary:
            char_dictionary[char] += 1
        else:
            char_dictionary[char] = 1
    return char_dictionary

def sort_on(items):
    return items["num"]

def sort_char_dict(char_dict):
    list_char_dict = []
    for char in char_dict:
        if char.isalpha():
            list_char_dict.append({"char":char, "num": char_dict[char]})
    list_char_dict.sort(reverse=True, key=sort_on)
    return list_char_dict