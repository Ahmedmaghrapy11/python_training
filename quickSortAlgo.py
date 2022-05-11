# partitioning function used in quick sort algorithm

# first way of partitioning
def partition1(arr, iBegin, jEnd):

    i = iBegin
    j = jEnd
    pivLoc = i

    while True:
        
        while arr[pivLoc] <= arr[j] and pivLoc != j:
            j = j -1
            if pivLoc == j:
                break
            elif arr[pivLoc] > arr[j]:
                arr[j], arr[pivLoc] = arr[pivLoc], arr[j]
                pivLoc = j
        
        while arr[pivLoc] >= arr[i] and pivLoc != i:
            i = i + 1
            if pivLoc == i:
                break
            elif arr[pivLoc] < arr[i]:
                arr[i], arr[pivLoc] = arr[pivLoc], arr[i]
                pivLoc = i
                return pivLoc
    
# second way of partitioning
def partition2(arr, l, h):
    
    p = arr[l]
    i = l
    j = h

    while i < j:
        
        while True:
            i = i + 1
            if (arr[i] > p):
                break
        
        while True:
            j = j - 1
            if(arr[i] <= p):
                break
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[j] = arr[j], arr[l]
            return j

# quick sort function

def quickSort(arr, l, h):
    if l < h:
        piv = partition2(arr, l, h)
        quickSort(arr, l, piv-1)
        quickSort(arr, piv+1, h)

# testing algorithm

array = [5,9,2,4,11,3]
n = len(array)

quickSort(array, 0, n)

for i in array:
    print(i , " ")