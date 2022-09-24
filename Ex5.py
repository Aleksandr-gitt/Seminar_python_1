# Напишите программу, которая принимает на вход число и проверяет, кратно ди оно 5 и 10 или 15
# но не 30:

number = int(input('Введите число: '))
if number % 30 != 0 and (number % 5 == 0 and number % 10 == 0 or number % 15 == 0):
    print('yes')
else:
    print('no')
