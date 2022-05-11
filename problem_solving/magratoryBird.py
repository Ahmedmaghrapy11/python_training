def magratoryBirds(arr):
    count = [0] * 6
    for i in arr:
        count[i] += 1
    return count.index(max(count))

# print(magratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))

count = [0] * 6
print(count)
print(count.index(max(count)))