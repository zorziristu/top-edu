
# 1


def sum(m):
    l = len(m)
    s = 0
    s1 = 0
    n1 = 0
    n2 = 0
    srArif = 0
    srArif1 = 0
    for i in range(l):
        if m[i] % 2 == 0:
            n1 += 1
            s += m[i]
        else:
            n2 += 1
            s1 += m[i]
    srArif = s // n1
    srArif1 = s1 // n2
    print(srArif)
    print(srArif1)


sum([3, 6, 2, 6, 5, 9, 2])


def kratnoe(ch, k):
    l1 = len(ch)
    ch1 = 0
    nn = 0
    sA = 0
    for i in range(l1):
        if ch[i] % k == 0:
            ch1 += ch[i]
            nn += 1

        else:
            print('yt ltktnmcz yf 9')
    sA = ch1 // nn
    print(sA)


kratnoe([81, 9, 4, 2, 18], 9)
#2 


def liniya (l,s):
    for i in range (l):
        print (s)

liniya(5, '%')


#3

def what (nomber):
    if nomber > 0:
        print ('Number is positive')
    if nomber < 0 :
        print ('Number is negative')
    if nomber == 0:
        print ('Number is equal to zero') 
    if nomber == 7:
        print ('Good bye!')       
        pass


what(7)


#4

c_max = 0
c_min = 0
while (True):
    chislo = int(input("Введите число - - "   ))
    if chislo  == 7:
        print("good bye") 
        break
    elif chislo > c_max:
        c_max = chislo
    
print (c_max)