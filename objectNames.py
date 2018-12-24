names = []
while True:
    print("Input the name of person " + str(len(names) + 1) + ", or input nothing to stop.")
    name = input()
    if(name == ''):
        break
    else:
        names += [name]

print("The object names are: ")
for name in names:
        print("    " + name)
