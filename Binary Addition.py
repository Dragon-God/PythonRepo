def reverse(s):
    n = len(s)
    c = n-1
    value = ""
    while c >= 0:
        value += s[c]
        c -= 1

    return value

def add_binary(a,b):
    sum = int(a) + int(b)
    var = True
    result = ""
    while(var):
        num = sum%2
        result += str(num)
        sum = sum//2
        if sum == 0:
            var = False

    return reverse(result)


print()
a = input()
b = input()
print(add_binary(a,b))
