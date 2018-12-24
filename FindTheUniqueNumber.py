def find_uniq(arr):
    pseudocount = {}    # Dictionary to count the number of elements in the array.
    for num in arr:
        pseudocount.setdefault(num, 0)
        pseudocount[num] += 1
        if len(pseudocount) > 1:    # When the two numbers in the array have been identified. 
            for index in pseudocount:
                if pseudocount[index] > 2:  # Delete the duplicate element.
                    del(pseudocount[index])
                    unique = list(pseudocount.keys())[0]    # The sole key of "pseudocount" is the unique number.
                    return unique
