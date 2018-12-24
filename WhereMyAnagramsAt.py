#Code Wars: Where my anagrams at? A program that finds all anagrams of "word" in "wordList".

def anagrams(word, wordList):
    result = [] #List to store all the anagrams.
    for i in wordList:  #Outer loop finds all anagrams of "word".
        source = list(i)   #Creates a copy of the current word in the word list as a list.
        var = True #Boolean value that indicates whether "i" is an anagram of "word" or not.
        for j in word:  #Inner loop. It checks if "i" is an anagram of "word".
            if j in source:    #Incrementally deletes the matching characters.
                source.remove(j)
            else:   #Early exit if a single character in "word" is missing from "i".
                var = False
                break
        if source != []:    #If "i" is an anagram of "word", then "source" should be empty.
            var = False
        if var:   #Add the word to the result list iff "i" is an anagram of "word".
            result.append(i)
    return result

                
