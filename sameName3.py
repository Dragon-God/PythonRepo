def spam():
    eggs = 'spam'
    global eggs
    eggs = "yolk"
    return

spam()
print(eggs)
