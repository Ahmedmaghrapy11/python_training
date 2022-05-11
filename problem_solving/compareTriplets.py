def compareTriplets(a, b):
    
    # Write your code here
    
    cpAlice = 0
    cpBob = 0
    finalScore = []
    
    for i1, i2 in zip(a,b):
            
        if i1 > i2:
            cpAlice = cpAlice + 1
        
        if i1 < i2:
            cpBob = cpBob + 1
        
        else:
            pass

    finalScore.append(cpAlice)
    finalScore.append(cpBob)
    
    return finalScore

x = [1,2,3]
y = [3,2,1]

print(compareTriplets(x,y))