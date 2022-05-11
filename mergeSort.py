#printing items in array using sleep() function.
from time import sleep
def printItems(arr):
    for i in arr:
        sleep(1)        #pauses the function work for 1 sec.
        print(i)
#printItems([2,4,6,8])

#multiplication of items in an array
def multiply(arr):
    for i in arr:
        for n in arr:
            n * arr[i+1]
            i += 1
            n += 1

print(multiply([2,4,6]))