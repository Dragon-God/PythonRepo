# Program that adds bullet points to text copied from the clipboard.

import pyperclip

text = pyperclip.paste()

print(text)
var = text.splitlines()

print(var)
for index in range(len(var)):
    var[index] = ('* ' + var[index])

print(var)
text2 = '\n'.join(var)

print(text2)
pyperclip.copy(text2)
