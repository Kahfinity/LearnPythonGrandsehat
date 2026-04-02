# Kalkulator Patungan Makan

# 1. INPUT
# Kita gunakan float karena harga bisa ada desimal
jumlah_makanan = float(input("Berapa total harga makanan? Rp "))

# Pajak di Indonesia biasanya 10%
pajak = float(input("Berapa persen pajak? (contoh 10) "))

# Biaya layanan biasanya 5% atau 10%
layanan = float(input("Berapa persen biaya layanan? (contoh 5) "))

# Jumlah orang harus bilangan bulat (int)
jumlah_orang = int(input("Berapa orang yang patungan? "))

# 2. PROSES (Hitung-hitungan)
# Hitung uang pajak
uang_pajak = jumlah_makanan * (pajak / 100)

# Hitung uang layanan
uang_layanan = jumlah_makanan * (layanan / 100)

# Total semua biaya
total_semua = jumlah_makanan + uang_pajak + uang_layanan

# Bagi rata ke setiap orang
bayar_per_orang = total_semua / jumlah_orang

# 3. OUTPUT (Menampilkan hasil)
#:.2f agar ada 2 angka di belakang koma
print("\n--- Rincian Biaya ---")
print(f"Total Makanan : Rp {jumlah_makanan:,.2f}")
print(f"Pajak         : Rp {uang_pajak:,.2f}")
print(f"Layanan       : Rp {uang_layanan:,.2f}")
print(f"Total Bayar   : Rp {total_semua:,.2f}")
print("-" * 25)
print(f"Tiap orang bayar: Rp {bayar_per_orang:,.2f}")