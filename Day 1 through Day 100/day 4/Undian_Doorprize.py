import random

peserta = ["Andi", "Budi", "Citra", "Dewi", "Eka", "Fajar", "Gita"]

# Ambil 3 pemenang unik sekaligus
pemenang = random.sample(peserta, 3)

print("🏆 HASIL UNDIAN")
for i, nama in enumerate(pemenang, start=1):
    print(f"Juara {i}: {nama}")