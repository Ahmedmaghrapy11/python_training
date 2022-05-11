import math

def gradingStudents(grades):
    # Write your code here
    
    newGrade = 0
    newGrades = []
    base = 5
    nextMultipleOf5 = []

    for grade in grades:
        x = math.ceil(grade / 5.0) * 5
        nextMultipleOf5.append(x)

    for grade in grades:
        i = grades.index(grade)
        if grade < 38:
            newGrades.append(grade)
        elif nextMultipleOf5[i] - grade < 3:
            newGrade = nextMultipleOf5[i]
            newGrades.append(newGrade)
            i += 1
        elif nextMultipleOf5[i] - grade >= 3:
            newGrades.append(grade)
            i += 1
    return newGrades

arr = [73, 67, 38, 33]
print(gradingStudents(arr))