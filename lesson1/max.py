def max(g):
    r = g[0]
    for i in range(len(g)):
        a = g[i]
        if a > r:
            r = a
    return r


print(max([23, 5, 7, 2, 1, 7, 98, 4, 3, 2]))
