#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2


n = int(input('Введите количество монет '))
o = 0
r = 0
for i in range(n):
    x = int(input('Введите (1) если орел или (0) если решка '))
    if x == 1:
        o += 1
    else:
        r += 1
if o <= r:
    print(f'Переверните {o} монет с орла на решку')

else:
    print((f'Переверните {r} монет с решки на орла'))