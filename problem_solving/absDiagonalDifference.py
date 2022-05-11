# function
def diagonalDifference(arr):
    # Write your code here

    # list comperhension method
    # n = len(arr)
    # d1 = sum([arr[x][x] for x in range(len(arr))])
    # d2 = sum([arr[x][n - 1 - x] for x in range(len(arr))])
    # return(abs(d1 - d2))

    # ordinary method 
    ltrDiagonalSum = 0
    rtlDiagonalSum = 0
    n = len(arr)

    for x in range(len(arr)):
        ltrDiagonalSum = ltrDiagonalSum + arr[x][x]
    
    for y in range(len(arr)):
        rtlDiagonalSum = rtlDiagonalSum + arr[y][n - 1 - y]
    
    absDiff = abs(ltrDiagonalSum - rtlDiagonalSum)
    return absDiff

# testing function
myMatrix = [ [1,2,3], [4,5,6], [9,8,9] ]

print(diagonalDifference(myMatrix))