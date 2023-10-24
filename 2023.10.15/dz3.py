def what():
    n = int(input("число "))
    while n != 7:
        if n > 0:
            print('Number is positive')
        elif n < 0:
            print('Number is negative')
        else:
            print('Number is equal to zero')
        n = int(input("число "))
    print('Good bye!')

what()
