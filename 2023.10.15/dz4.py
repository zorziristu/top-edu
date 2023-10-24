chislo = int(input("Введите число - - "))
c_min = chislo
c_max = chislo
while (True):
    if chislo == 7:
        print("good bye")
        break
    elif c_max < chislo:
        c_max = chislo
    elif c_min > chislo:
        c_min = chislo
    chislo = int(input("Введите число - - "))

print('минимальное ', c_min)
print('максимальное ', c_max)
