def spam(divideBy):
    try:
        var = 42 / divideBy
        if int(var) == var:
            var = int(var)
    except ZeroDivisionError:
        var = "You can't divide a number by zero."
    return var   
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
