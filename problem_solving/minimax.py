def miniMaxSum(arr):

    arr.sort()
    s = sum(arr)
    maxValSum = s - arr[0]
    minValSum = s - arr[len(arr) - 1]
    print(minValSum, maxValSum)

    # minValSum = 0
    # maxValSum = 0

    # minNum = min(arr)
    # maxNum = max(arr)

    # for i1 in arr:
    #     if not i1 == maxNum:
    #         minValSum += i1

    # for i2 in arr:
    #     if not i2 == minNum:
    #         maxValSum += i2

    # print(minValSum, ' ', maxValSum)

arr = [5,5,5,5,5]
miniMaxSum(arr)