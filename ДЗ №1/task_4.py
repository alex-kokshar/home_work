num = int(input('Введите целое положительное число: '))
max_num = 0

while True:
    i = num % 10

    if i > max_num:
        max_num = i
    num = int(num / 10)

    if num == 0:
        break

print('Максимальная цифра в числе:', max_num)
