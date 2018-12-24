#"Code Wars: Count the number of Duplicates".
#A function that counts the number of distinct case insensitive alphabetic characters and numeric digits that occur more than once in an input string.

from collections import Counter

def duplicate_count(text):
    text = text.lower()
    result = 0
    var = Counter(text)     
    for char in var:
        if var[char] > 1:
            result += 1
    return result
