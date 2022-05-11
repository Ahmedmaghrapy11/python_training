def plusMinus(arr):
    # Write your code here
    n = len(arr)
    posNums = 0
    negNums = 0
    zeros = 0
    
    for i1 in arr:
        if i1 > 0:
            posNums = posNums + 1
        elif i1 < 0:
            negNums = negNums + 1
        else:
            zeros = zeros + 1

    posRatio = posNums / n
    negRatio = negNums / n
    zeroRatio = zeros / n
    
    print(f"{'{:.6f}'.format(posRatio)}\n{'{:.6f}'.format(negRatio)}\n{'{:.6f}'.format(zeroRatio)}")

array = [1,1,0,-1,-1]

plusMinus(array)