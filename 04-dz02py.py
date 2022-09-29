# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.


n = int(input('Введите число '))
list = []

for i in range(-n,n+1):
    list.append(i)
print(f'Заданный список: {list}')

result = 1
with open('file.txt','w') as data: #позиции жестко заданы
    data.write('1 \n')
    data.write('3 \n')
    data.write('4 \n')
    data.write('0 \n')
    data.write('6 \n')

positions = 'file.txt'
data = open(positions, 'r')

for line in data:
    pos = int(line)
    result *= list[pos]
print(f'Произведение элементов на заданных позициях: {result}')