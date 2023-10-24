def sum(r1, r2):
    chet = 0
    not_chet = 0
    kl_chet = 0
    kl_not_chet = 0
    chet_srArif = 0
    not_chet_srArif = 0
    for i in range(r1, r2+1):
        if i % 2 == 0:
            kl_chet += 1
            chet += i
        else:
            kl_not_chet += 1
            not_chet += i
    chet_srArif = chet / kl_chet
    not_chet_srArif = not_chet / kl_not_chet
    s_o = chet + not_chet
    s_o_srArif = s_o / (kl_chet + kl_not_chet)

    print('сумма четных ', chet)
    print('сред.арифметик. четных  ', chet_srArif)

    print('сумма нечетных ', not_chet)
    print('сред.арифметик. нечетных ', not_chet_srArif)

    print('общая сумма ', s_o)
    print('общая сред.арифметик.', s_o_srArif)


def kratnoe(r1, r2, k):
    sum = 0
    kl = 0
    for i in range(r1, r2+1):

        if i % k == 0:
            sum += i
            kl += 1

    sA = '?'
    if kl > 0:
        sA = sum / kl

    print('сумма кратных ', k, ' ', sum)
    print('сред.арифметик. кратных', k, ' ', sA)


r1 = int(input('от '))
r2 = int(input('до '))
sum(r1, r2)
kratnoe(r1, r2, 9)
