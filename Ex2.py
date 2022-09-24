# Напишите программу которая принимает 5 чисел и находит самое большое:

numbers = []
i = 0
while i < 5:
    number = int(input('Введите число: '))
    numbers.append(number)
    i += 1
print(numbers)
j = 0
num = 0
while j < 5:
    if num < numbers[j]:
        num = numbers[j]
    j += 1

print(num)