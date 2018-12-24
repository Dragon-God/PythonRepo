import pprint

def char_count(string):
    result = {}
    for char in string:
        result.setdefault(char, 0)
        result[char] += 1
    return result

