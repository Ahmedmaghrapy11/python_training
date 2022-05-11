def solution(arr):
    x = 1
    y = set(arr)
    while True:
        if x not in y:
            return x
        x = x + 1

a = [1 , 2 , 3]
print(solution(a))