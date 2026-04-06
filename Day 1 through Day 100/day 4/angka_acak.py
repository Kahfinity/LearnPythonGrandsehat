import random

# Generate 5 angka acak
angka_acak = [random.randint(10, 99) for _ in range(5)]

# Urutkan
angka_acak.sort()

# Analisis
minimum = angka_acak[0]
maksimum = angka_acak[-1]
rata_rata = sum(angka_acak) / len(angka_acak)
ada_50 = 50 in angka_acak

print(f"Data: {angka_acak}")
print(f"Min: {minimum} | Max: {maksimum} | Rata-rata: {rata_rata:.2f}")
print(f"Angka 50 ada? {ada_50}")