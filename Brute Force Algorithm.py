# Brute Force (Mencari nilai maksimum)

data = [12, 45, 7, 89, 23]

max_value = data[0]

for i in data:
    if i > max_value:
        max_value = i

print("Nilai terbesar =", max_value)