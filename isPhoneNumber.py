def phone_number(string):
    if len(string) != 12:
        return False
    else:
        text = string.split('-')
        if len(text) != 3:
            return False
        else:
            for word in text:
                if not(word.isdecimal()):   # If one of the three elements of text is not a number.
                    return False
            if len(text[0]) != 3:
                return False
            elif len(text[1]) != 3:
                return False
            elif len(text[2]) != 4:
                return False
            else:
                return True

def find_phone_no(text):
    var = False
    length = len(text)
    if length >= 12:
        for i in range(length)
            chunk = text[i:1+12]
            if phone_number(chunk):
                print('Phone number found: ' + chunk)
                var = True
    if not(var):
        print('No phone number found.')
