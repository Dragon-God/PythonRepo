def find_next_square(sq):
    var1 = sq**(0.5)
    var2 = int(var1)
    if var2 != var1:
        return -1
    else:
        return ((var2+1)**2)

print(find_next_square(121))
