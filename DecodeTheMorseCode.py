# "Code Wars: Decode the Morse Code"

def decodeMorse(morse_code):
    clear_text = ''
    char = ''
    index = 0
    length = len(morse_code)
    delim1 = " "    # Next character delimiter.
    delim2 = "   "  # Next word delimiter. 
    while index < (length):   
        if morse_code[index] != delim1:
            # Build the character to be added to the clear text.
            char += morse_code[index]
        else:
            # When the delimiter is encountered.
            clear_text += MORSE_CODE[char]
                # Add said character to clear text
            char = ''
                # Reset "char".
            if index < (length-2):
                # If it is possible to encounter a space.
                if morse_code[index:(index+3)] == delim2:
                    # When a space is encountered.
                    clear_text += " "
                    index += 2
                    if index == length-1:
                        # If the last character in the code is a space, assign a control value to "char"
                        char = ""
        index += 1

    if char != "":
        # If the last character isn't a space.
        clear_text += MORSE_CODE[char]
            # Add the final character to the clear text.
    return clear_text
        
        
