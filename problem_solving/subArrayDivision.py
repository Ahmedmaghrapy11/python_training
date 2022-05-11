def subArrayDivision(s, d, m):
    
    # your code goes here

    count = 0
    for i in range(m, len(s) + 1):
        if sum(s[i-m:i]) == d:
            count += 1
    return count

    # numOfWays = 0
    # shared = []
    
    # for i in s:
    #     for j in s:
    #         shared.append(i)
    #         shared.append(j)
            
    #         if len(shared) == m and sum(shared) == d:
    #             if shared != shared:
    #                 numOfWays = numOfWays + 1
                
    #         shared.pop(0)
    #         shared.pop(0)

    # return numOfWays

print(subArrayDivision([1,2,1,3,2], 3 ,2))
