# Greedy Algorithm (Coin Change)

coins = [1000, 500, 200, 100, 50]
amount = 2750

result = []

for coin in coins:
    while amount >= coin:
        amount -= coin
        result.append(coin)

print("Koin yang digunakan:", result)