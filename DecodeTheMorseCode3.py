def decodeMorse2(morse_code):
    clear_text = ''
    char = ''

    for index, di_dah in enumerate(morse_code.strip() + ' '):
        if di_dah != ' ':
            char += di_dah
        elif char:
            clear_text += MORSE_CODE[char]
            char = ''
            if index < len(morse_code) - 2:
                if morse_code[index: index + 3] == '   ':
                    clear_text += " "

    return clear_text    
