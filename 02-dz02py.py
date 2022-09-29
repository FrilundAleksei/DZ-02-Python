# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input('Введите число N: '))
factorial = 1
for i in range(1, N+1):
    factorial *= i
    print(factorial, end=', ')


# можно через функцию

# def factorial (number, count = 1):
#     for i in range(1, number + 1):
#         count *= i
#     return count

# N = int(input('Enter the number: '))
# print(f'Произведений чисел от 1 до {N} = [ ', end = '')
# for i in range(1, N + 1):
#     if i == N: 
#         print(f'{factorial(i)}')
#     else:
#         print(f'{factorial(i)}', end = ', ')

