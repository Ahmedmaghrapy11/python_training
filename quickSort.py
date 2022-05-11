def quickSort(arr):
    if len(arr) < 2:    #base case of quicksort algorithm
        return arr
    else:
        pivot = arr[0]      #recursive case of quicksort algorithm
        less = [i for i in arr[1:] if i <= pivot]   #sub-array of all elements less than pivot
        greater = [i for i in arr[1:] if i > pivot]     #sub-array of all elements greater than pivot
    return quickSort(less) + [pivot] + quickSort(greater)   #combining sorted elements

print(quickSort([30 , 10 , 40, 90 ,20]))        #testing algorithm