def remove_smallest(numbers):
    n =len(numbers)
    result = [None]*(n-1) #empty array to store the result to be returned by the function.
    if n == 0:  #Testing if the list is empty
        return []
    else:     
        mini = [0,numbers[0]]   #List to store the minimum element (and its position) in the list.
        
        for i in range(1,n):    #Loop to find th minimum element in the list.
            if mini[1] > numbers[i]:
                mini[0] = i
                mini[1] = numbers[i]

        c1 = 0   #Variable to track the position in 'result'.
        c2 = 0   #Variable to track the position in 'numbers'.
        while c2 < n:
            if c2 == mini[0]:
                c2 += 1
                continue
            result[c1] = numbers[c2]
            c2 += 1
            c1 += 1

    return result

print(remove_smallest([1,2,3,4,5]))
