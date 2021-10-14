# Coin Dispensing
# The minimum number of coins to spend a certain amount using the selected denominations

from math import inf

def coin_dispensing(denominations, amount):
    f = [inf for _ in range(amount + 1)]
    p = [[] for _ in range(amount + 1)]
    denominations.sort()
    for i in range(denominations[0]):
        f[i] = 0
    for coin in denominations:
        for j in range(denominations[0], amount + 1):
            if coin <= j:
                if f[j] > f[j-coin]+1:
                    f[j] = f[j-coin]+1
                    p[j] = p[j - coin] + [coin]

    return f[amount], p[amount]


coin_denominations = [1, 5, 8]
amount_to_spend = 12
counter, result = coin_dispensing(coin_denominations, amount_to_spend)
print(f"Amount of coin: {counter}\nIt's: {result}")









