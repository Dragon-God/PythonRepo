def DNA_strand(dna):
    n1 = len(dna)
    var = ""
    if dna[0] != 'A' and dna[0] != 'C' and dna[0] != 'G' and dna[0] != 'T':
        count = 7
        while(dna[count] == 'A' or dna[count] == 'C' or dna[count] == 'G' or dna[count] == 'T'):
            var += dna[count]
            count += 1
    else:
        var = dna
    n2 = len(var)    
    result = ""
    count = 0
    while count < n2:
        if var[count] == 'T':
            result += 'A'
        elif var[count] == 'A':
            result += 'T'
        elif var[count] == 'G':
            result += 'C'
        elif var[count] == 'C':
            result += 'G'
        count += 1

    return result

print()
value = input()
print(DNA_strand(value))

           
