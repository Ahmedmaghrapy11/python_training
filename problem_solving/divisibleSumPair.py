def divisibleSumPairs(n, k, ar):
    # Write your code here
    count = 0
    for i in range(n-1):
        j = i + 1
        while j < n:
            if ((ar[i] + ar[j]) % k) == 0:
                count += 1
            j += 1
    return count

# 0     1     2     3      4      5
######################################## 
# 1     2     3     4      5      6

print(divisibleSumPairs(6, 5, [1,2,3,4,5,6]))