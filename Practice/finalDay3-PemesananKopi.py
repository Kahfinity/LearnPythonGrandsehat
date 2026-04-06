print("☕ Selamat datang di Kafe Python! ☕")

nama_pelanggan = input("Siapa nama Anda? ")
jumlah_pesanan = input("Berapa gelas kopi yang Anda pesan? ")

nama_pelanggan = nama_pelanggan.strip().title()

jumlah_pesanan = int(jumlah_pesanan)

ukuran_kopi = input("Pilih ukuran (S/M/L): ").upper()

if ukuran_kopi == "S":
    harga_dasar = 15000
elif ukuran_kopi == "M":
    harga_dasar = 25000
elif ukuran_kopi == "L":
    harga_dasar = 35000
else:
    print("Ukuran tidak dikenali!!. Otomatis Menggunakan ukuran Medium.")
    harga_dasar = 25000
    ukuran_kopi = "M"

tambahan_susu = input("Tambah susu? (ya/tidak): ").lower()
tambahan_gula = input("Tambah gula? (ya/tidak): ").lower()

if tambahan_susu == "ya" and tambahan_gula == "ya":
    tambahan_harga = 5000
elif tambahan_susu == "ya" or tambahan_gula == "ya":
    tambahan_harga = 3000
else:
    tambahan_harga = 0

total_harga = (harga_dasar + tambahan_harga) * jumlah_pesanan

print("\n" + "="*30)
print(f"🧾 STRUK PEMESANAN")
print("="*30)
print(f"Nama    : {nama_pelanggan}")
print(f"Pesanan : {jumlah_pesanan}x Kopi {ukuran_kopi}")
print(f"Total   : Rp {total_harga}")
print("="*30)
print("Terima kasih! Semoga hari Anda menyenangkan.")