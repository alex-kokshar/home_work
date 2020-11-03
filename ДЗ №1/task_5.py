profit = int(input('Введите сумму выручки: '))
wasted = int(input('Введите сумму издержек: '))

if profit > wasted:
    print('Компания в прибыли. Рентабельность', round((profit - wasted) * 100 / profit), '%')
    crew = int(input('Кол-во сотрудников: '))
    print('Прибыль фирмы на 1 сотрудника', round((profit - wasted) / crew), '$')
else:
    print('Компания в убытке')
