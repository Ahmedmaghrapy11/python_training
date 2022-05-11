def unbounded_knapsack(w, n, val, wt):
    
    # max_val[i] is going to store maximum
    # value with knapsack capacity i
    max_val = [0 for i in range(w + 1)]
    ans = 0
    
    # Fill max_val[] using above recursive formula
    for i in range(w + 1):      # w = 100
        for j in range(n):      # n = 3
            if wt[j] <= i:      # 
                max_val = max(max_val[i], (max_val[i - wt[j]] + val[j]))
    
    return max_val[w]

w = 100
val = [10,30,20]
wt = [5,10,15]
n = len(val)

print(unbounded_knapsack(w,n,val,wt))