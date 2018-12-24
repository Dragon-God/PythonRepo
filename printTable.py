def print_table(table):     # Prints a list of lists in tabular form.
    # Each of the the elements of "table" is a list and represents one of the columns of the table.
    maxx = 0.
    col_width = []
    total_width = 0
    lengthX = len(table)
    for element in table:   # Find the number of rows the table will have.
        length = len(element)
        maxx = length if length > maxx else maxx     

    for element in table:   # Loop to seed the sub lists so that they all have the same length.
        length = len(element)
        if length < maxx:
            for i in range(length, maxx):
                element.append('None')

    for i in range(lengthX):   # Find the width of the table columns.
        width = 0
        for j in range(maxx):
            length = len(table[i][j])
            width = length if length > width else length
        width += 2
        col_width.append(width)

    for width in col_width:
        total_width += width

    print('_'*(total_width+(lengthX*2)))
    for i in range(maxx):
        for j in range(lengthX):
            print(str(table[j][i]).ljust(col_width[j]) + ' |', end='')
        print()
        print('_'*(total_width+(lengthX*2)))
        
text = "Write a function named printTable()"
var = []
for word in text.split():
    var.append(list(word))

print_table(var)
