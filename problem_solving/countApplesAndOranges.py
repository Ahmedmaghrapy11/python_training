# first solution
def countApplesAndOranges(startP, endP, appTree, orTree, apples, oranges):
    # start your code here
    
    appLoc = []
    orLoc = []
    appleDist = 0
    orangeDist = 0
    appleNums = 0
    orangeNums = 0

    for apple in apples:
        appleDist = apple + appTree
        appLoc.append(appleDist)

    for orange in oranges:
        orangeDist = orange + orTree
        orLoc.append(orangeDist)

    for apple in appLoc:
        if apple >= startP and apple <= endP:
            appleNums = appleNums + 1
        else:
            pass
    
    for orange in orLoc:
        if orange <= endP and orange > startP:
            orangeNums = orangeNums + 1
        else:
            pass
    
    print(f"{appleNums}\n{orangeNums}")

# second solution
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_Apples = 0
    count_Oranges= 0

    for i in range(len(apples)):
        if a+apples[i] >= s and a+apples[i] <= t:
            count_Apples +=1

    for i in range(len(oranges)):
        if b+oranges[i] >= s and b+oranges[i] <=t:
            count_Oranges +=1
            
    print(count_Apples)
    print(count_Oranges)

applesList = [2,3,-4]
orangesList = [3,-2,-4]
sP = 7
eP = 10
aT = 4
oT = 12
countApplesAndOranges(sP, eP, aT, oT, applesList, orangesList)