# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го
# члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

values=tuple(map(int, input('Введите первый элемент, разность и количество элементов арифметической прогрессии через пробел: ').split()))
list=[i for i in range(values[0],values[0]+(values[2]-1)*values[1]+1,values[1])]
print(list)

