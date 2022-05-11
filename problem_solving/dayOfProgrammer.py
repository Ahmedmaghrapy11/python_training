def dayOfProgrammer(year):
    # Write your code here
    dayOfProgrammer = 256
    firstEightMonths = 243
    resultDay = 0
    
    if year == 1918:
        return '26.09.1918'
    elif year >= 1700 and year <= 1917:
        if year % 4 == 0:
            resultDay = dayOfProgrammer - (firstEightMonths + 1)
            resultDate = f"{str(resultDay)}.09.{str(year)}"
            return resultDate
        else:
            resultDay = dayOfProgrammer - firstEightMonths
            resultDate = f"{str(resultDay)}.09.{str(year)}"
            return resultDate
    elif year >= 1918:
        if year % 400 == 0 or (year % 4 == 0 and not (year % 100 == 0)):
            resultDay = dayOfProgrammer - (firstEightMonths + 1)
            resultDate = f"{str(resultDay)}.09.{str(year)}"
            return resultDate
        else:
            resultDay = dayOfProgrammer - firstEightMonths
            resultDate = f"{str(resultDay)}.09.{str(year)}"
            return resultDate

print(dayOfProgrammer(1800))