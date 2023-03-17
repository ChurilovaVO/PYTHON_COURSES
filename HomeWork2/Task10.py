# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint
quantity=int(input('Введите число монеток: '))
count=0
eagle=0
tails=0
while count<quantity:
    coin=randint(0,1)
    if coin==0:
        eagle+=1
    else:
        tails+=1
    count+=1
    print(coin, end=' ')
print()
if eagle==tails:
    print(f'Монетки лежат по ровну по {eagle}')
elif eagle<tails:
    print(f'Орлом вверх лежит {eagle} монет')
else:
    print(f'Решкой вверх лежит {tails} монет')


    