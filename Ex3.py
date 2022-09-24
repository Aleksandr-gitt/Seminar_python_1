# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N:

N = int(input('Введите число: '))
num = N * -1
while num < N+1:
    print(num)
    num +=1

# numbers = []
# while num < N+1:
#     numbers.append(num)
#     num += 1

# print(numbers)