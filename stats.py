def get_num_words(contents):
    words = contents.split()
    return len(words)

def get_char_count(contents):
    #takes a string and counts the number of times each character is in the string
    character_dict = {}
    for c in contents:
        if c.lower() not in character_dict.keys():
            character_dict[c.lower()] = 1
        else:
            character_dict[c.lower()] += 1
    return character_dict

def sort_on(items):
    return items["num"]

def get_sorted(my_dict):
    new_list = []
    for c in my_dict.keys():
        new_list.append({"char": c, "num": my_dict[c]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list