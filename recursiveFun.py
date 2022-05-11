def countDown(i):
    print(i)
    if (i <= 0):
        return 0
    else:
        countDown(i-1)

countDown(20)