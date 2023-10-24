def imp ():
    s2 = 0
    s = 0
    s1 = 0
    k=[-23, 3, -43, 50, -9, 23, 89]
    h=len(k)
    for i in range (h):
        if k[i] < 0:
            s += k[i]
        else:
            s1 += k[i]    
    s2 = s + s1
    print(s2)
imp()

