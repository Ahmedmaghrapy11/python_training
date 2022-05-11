def breakingRecords(scores):
    # Write your code here
    
    highestBreak = scores[0]
    lowestBreak = scores[0]
    highBreakTimes = 0
    lowBreakTimes = 0
    breakList = []

    # get breaking highest record times
    for i in scores:
        if i > highestBreak:
            highBreakTimes = highBreakTimes + 1
            highestBreak = i
    breakList.append(highBreakTimes)
    
    # get breaking lowest record times
    for i in scores:
        if i < lowestBreak:
            lowBreakTimes = lowBreakTimes + 1
            lowestBreak = i
    breakList.append(lowBreakTimes)

    return breakList

print(breakingRecords([10,5,20,20,4,5,2,25,1]))
