# "Code Wars: Stop gninnipS My sdroW!"
# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed
# (Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.

def reverse(string):
    result = ""
    count = 1
    length = len(string)
    if length > 0:
        while count <= length:
            result += string[-count]
            count += 1
    return result

def spin_words(text, delim=" "):    # Function to explode a string in Python.
    result = ''
    word = ''
    for char in text:
        if char != delim:   # Grow the "word" string while the current character is not the delimiter.
            word += char
        else:   # When the delimiter is encountered.
            if len(word) < 5:   # Add short words normally.
                result += word
            else:   # Add long words reversed.
                result += reverse(word)
            result += char  # Add the delimiter.
            word = ''   # Reset "word".
            
    if len(result) != len(text):    # Due to the else clause depending on encountering the delimiter to add the word.
        if len(word) < 5:   # Add short words normally.
                result += word
        else:   # Add long words reversed.
            result += reverse(word)
    return result

