# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
import random

coins = int(input("Введите количество монет = "))
coin = []
for i in range(coins):
    temp = random.randint(0, 1)
    coin.append(temp)
print(coin)

orel_coin = 0
reshka_coin = 0  
for temp in coin:
    if temp == 0:
        orel_coin += 1
    else:
        reshka_coin += 1
 
if orel_coin > reshka_coin or orel_coin == reshka_coin:
        count = coins - orel_coin

else:
        count = coins - reshka_coin
print (count, " - минимальное количество, которые нужно перевернуть")