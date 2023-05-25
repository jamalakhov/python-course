# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

def min_coin_flips(coins):
    heads = sum(coins)
    tails = len(coins) - heads

    return min(heads, tails)

n = int(input("Enter the number of coins: "))
coins = []
for _ in range(n):
    coin = int(input("Enter 0 for tails or 1 for heads: "))
    coins.append(coin)

min_flips = min_coin_flips(coins)
print("Minimum number of coin flips needed:", min_flips)