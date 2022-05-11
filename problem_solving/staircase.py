def staircase(n):
    for stairs in range(1, n + 1):
        print(' ' * (n - stairs) + '#' * stairs)

    # h = n
    # w = n
    # x = w - h + 1

    # while h <= n and w <= n:
    #     if h == 0 and w == 0:
    #         break
    #     else:
    #         if x == n:
    #             print(x * '#')
    #             x = x + 1
    #         elif x > n:
    #             break
    #         else:
    #             print((w - 1) * ' ', x * '#', ' ')
    #             h = h - 1
    #             w = w - 1
    #             x = x + 1

staircase(6)
