def getTotalX(a, b):
    # Write your code here
    maxA = max(a)
    minB = min(b)
    count = 0
    for num in range(maxA, minB + 1):
        # return boolean value
        left = all([num % numA == 0 for numA in a])
        right = all([numB % num == 0 for numB in b])
        # count all true values
        count += left * right
    return count

getTotalX([2, 4], [16, 32, 96])

a = [1,2,3]
x = [i == i+1 for i in a]

print(all(x))