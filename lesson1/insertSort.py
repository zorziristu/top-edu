a = [2, 34, 23, 9, 98, 1, 97]
for i in range(1, len(a)):
    t = a[i]
    j = i - 1
    while (j >= 0 and t < a[j]):
        a[j + 1] = a[j]
        a[j] = None
        j = j - 1
    a[j + 1] = t

print(a)

