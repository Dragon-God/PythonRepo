#"Code Wars: Where my anagrams at?" A program that finds all anagrams of "word" in "wordList".

def anagrams(word, words):
    result = [] #List to store all the anagrams.
    for other_word in words:  #Outer loop finds all anagrams of "word".
        if Counter(other_word) == Counter(word):
            result.append(other_word)
    return(result)
