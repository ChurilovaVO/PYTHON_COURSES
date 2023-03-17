# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

number=int(input('Введите число: '))
num=1
while num<number:
    num*=2
    if num<number:
        print(num, end =' ')

