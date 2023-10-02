# есть массив из чисел - и + надо сделать так что-бы - и + чисел было по ровну:

g = [-34, -987, 90, 23, -56, 9, -1, 34, 6, 7, 10]
f = len(g)
s = []
s1 = []
for i in range(f):
    if g[i] < 0:
        s.append(g[i])
    else:
        s1.append(g[i])

print(s)
print(s1)

x = len(s)
m = len(s1)
if x > m:
    u = x - m
    for i in range(u):
        s1.append(1)
elif m > x:
    d = m - x
    for j in range(d):
        s.append(-1)
# else:
#    pass - нечего не делать

t = s + s1
print(t)
