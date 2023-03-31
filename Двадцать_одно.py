import random
from random import randint

cards = [6, 7, 8, 9, 10, 2, 3, 4, 11]
flag = 0
    

while 1:
    k1 = randint(0, 8)
    k2 = randint(0, 8)
    k3 = randint(0, 8)
    k4 = randint(0, 8)
    k5 = randint(0, 8)
    k6 = randint(0, 8)
    k7 = randint(0, 8)
    k8 = randint(0, 8)
    
    print("\n" * 10)
    print('НОВАЯ ИГРА')
    print('Ваши очки:', cards[k1])
    summ = cards[k1]
    print('Взять еще карту введите +')
    print('Оставить введите -')
    a = input()
    if a == '+':
        print('Ваши очки:', cards[k2])
        summ += cards[k2]
        print('Сумма ваших очков:', summ)
        print('Взять еще карту введите +')
        print('Оставить введите -')
        b = input()
        if b == '+':
            print('Ваши очки:', cards[k3])
            summ += cards[k3]
            print('Сумма ваших очков:', summ)
            if summ <= 19:
                print('Взять еще карту введите +')
                print('Оставить введите -')
                c = input()
                if c == '+':
                    print('Ваши очки:', cards[k4])
                    summ += cards[k4]
                    print('Сумма ваших очков:', summ)
                    flag = 1
                    summ2 = cards[k5] + cards[k6] + cards[k7] + cards[k8]

                if c == '-':
                    flag = 1
                    summ2 = cards[k5] + cards[k6] + cards[k7]
                if c != '-' and c != '+':
                    print('Не то')

        if b == '-':
            flag = 1
            summ2 = cards[k5] + cards[k6]
        if b != '-' and b != '+':
            print('Не то')

    if a == '-':
        flag = 1
        summ2 = cards[k5]
    if a != '-' and a != '+':
        print('Не то')

    if flag == 1:
        if  summ < 21 and summ2 < 21:
            print('Сумма очков противника:', summ2)
            if summ > summ2:
                print('Вы выиграли!')
            if summ < summ2:
                print('Вы проиграли!')
            if summ == summ2:
                print('Ничья!')
        if summ > 21:
            print('Вы проиграли! Сумма ваших очков превышает 21')
        if summ2 > 21:
            print('Вы выиграли! Сумма очков противника превышает 21')