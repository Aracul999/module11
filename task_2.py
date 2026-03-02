#   Задача 2. Слишком большие числа
#   Что нужно сделать
#   Напишите программу, которая считала бы, сколько цифр во вводимом числе
#   Учтите, что программа должна получать только положительные числа
#   Что число 0 имеет одну цифру.


payment =int(input("Введите сумму счёта для оплаты: "))
while payment > 0:
    if payment >= 10 and payment <= 99:
        print('2-цифры')
        break
    if payment >= 100 and payment <= 999:
        print('3-цифры')
        break
    if payment >= 1000 and payment <= 9999:
        print('4-цифры')
        break
    if payment >= 10000 and payment <= 99999:
        print('5-цифры')
        break
    if payment >= 100000 and payment <= 999999:
        print('6-цифр')
        break
    if payment >= 1000000 and payment <= 9999999:
        print('7-цифр')
        break
    if payment >= 10000000 and payment <= 99999999:
        print('8-цифр')
        break
    if payment >= 100000000 and payment <= 999999999:
        print('9 -цифр')
        break
    if payment >= 1000000000 and payment <= 9999999999:
        print('10-цифр')
        break
    if payment >= 10000000000 and payment <= 99999999999:
        print('11-цифр')
        break
    if payment >= 100000000000 and payment <= 999999999999:
        print('12 -цифр')
        break
    if payment >= 1000000000000 and payment <= 9999999999999:
        print('13-цифр')
        break
    if payment >= 10000000000000 and payment <= 99999999999999:
        print('14-цифр')
        break
    if payment >= 100000000000000 and payment <= 999999999999999:
        print('15-цифр')
        break
    if payment >= 1000000000000000 and payment <= 9999999999999999:
        print('16-цифр')
        break
    if payment >= 10000000000000000 and payment <= 99999999999999999:
        print('17-цифр')
        break
    if payment >= 100000000000000000 and payment <= 999999999999999999:
        print('18-цифр')
        break
    if payment >= 1000000000000000000 and payment <= 9999999999999999999:
        print('19-цифр')
        break
    if payment >= 10000000000000000000 and payment <= 99999999999999999999:
        print('20-цифр')
    if payment == 0:
        print('1-цифра')
        break
    if payment <= 9 and payment >0:
        print('1-цифра')
        break
