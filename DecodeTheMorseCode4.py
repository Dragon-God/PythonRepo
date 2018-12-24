# Code Wars: Decode the Morse Code

def decodeMorse(morse_code):
    var1 = morse_code.strip().split('  ')
    var2 = []
    var3 = []
    for word in var1:  # A list of words in text.
        var2.append(word.split(' '))
    for sub_list in var2:  # A list of lists where the sublists contain the characters that make up the word.
        for i in range(len(sub_list)): 
            sub_list[i] = MORSE_CODE[sub_list[i]]   # Converting chars from morse code back to clear text.
        var3.append(''.join(sub_list))  # Generating the words from the text.
    return ' '.join(var3)
