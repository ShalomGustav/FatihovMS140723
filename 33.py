# Задача 30:  Заполните массив элементами
# арифметической прогрессии. Её первый
# элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения
# n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

n = int(input('Введите первый член АП'))
d = int(input('Введите разность АП'))
s = int(input('Введите количество элементов АП'))

an = [int(x) for x in range(n,s+1,d)]
print(an)

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума
# и не больше заданного максимума)

