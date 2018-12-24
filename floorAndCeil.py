#ceiling function "ceil()"
#return((int(x) + 1) if (x > int(x)) else (int(x)))

def floor(x):
    return(int(x))

def ceil(x):
    return((int(x) + 1) if (x > int(x)) else (int(x)))

print(ceil(5.5))
