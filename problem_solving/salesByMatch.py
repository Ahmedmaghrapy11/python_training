def sockMerchant(n, ar):
    # Write your code here
    pairs = 0
    color = set()
    for i in range(len(ar)):
        if ar[i] not in color:
            color.add(ar[i])
        else:
            pairs += 1 
            color.remove(ar[i])
    return pairs


print(sockMerchant(7,[1,2,1,2,1,3,2]))