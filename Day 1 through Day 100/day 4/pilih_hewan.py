hewan = ["Kucing", "Anjing", "Kelinci", "Hamster", "Burung"]
print(f"Daftar hewan: {hewan}")

idx = int(input("Masukkan indeks (0-4): "))

if 0 <= idx < len(hewan):
    print(f"Hewan di indeks {idx}: {hewan[idx]}")
else:
    print("Indeks tidak valid. Gunakan 0-4.")