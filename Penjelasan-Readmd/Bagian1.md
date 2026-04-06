# Day 1: Working with Variables in Python to Manage Data

## 1. Konsep Dasar Variabel di Python

### Apa Itu Variabel?
Variabel adalah **wadah bernama di memori komputer** yang digunakan untuk menyimpan data. Di Python, Anda tidak perlu mendeklarasikan tipe data secara eksplisit. Python menggunakan **dynamic typing**, artinya tipe data akan ditentukan otomatis saat nilai diberikan.

**Sintaks Penugasan (Assignment)**
```python
nama_variabel = nilai
```

**Contoh:**
```python
nama = "Andi"
usia = 21
tinggi = 175.5
aktif = True
```

### Aturan & Konvensi Penamaan

| Boleh | Tidak Boleh |
|--------|--------------|
| `nama_lengkap` | `2nama` (diawali angka) |
| `total_harga` | `total-harga` (menggunakan `-`) |
| `_data` | `class` (kata kunci Python) |
| `nilai1` | `nilai siswa` (mengandung spasi) |

> Python bersifat *case-sensitive* → `Nama` ≠ `nama`

### Tipe Data Dasar yang Wajib Dikuasai
| Tipe | Deskripsi | Contoh |
|------|-----------|--------|
| `int` | Bilangan bulat | `10`, `-5`, `0` |
| `float` | Bilangan desimal | `3.14`, `-0.75`, `2.0` |
| `str` | Teks/String | `"Halo"`, `'123'`, `" "` |
| `bool` | Nilai logika | `True`, `False` |

> **Tips Debugging:** Gunakan `type(variabel)` untuk memeriksa tipe data.
```python
print(type(usia))   # <class 'int'>
print(type(tinggi)) # <class 'float'>
```

---

## 2. Input, Output & Type Casting

| Fungsi | Deskripsi | Catatan Penting |
|--------|-----------|----------------|
| `print()` | Menampilkan data ke layar | - |
| `input()` | Membaca input dari user | **Selalu mengembalikan `str`** |
| `int()`, `float()`, `str()`, `bool()` | Type casting / konversi tipe data | Gunakan sebelum operasi matematika |

### Contoh Penggunaan Input & Casting:
```python
nama = input("Masukkan nama: ")          # str
usia_str = input("Masukkan usia: ")      # str
usia = int(usia_str)                     # konversi ke int

print(f"Halo {nama}, tahun depan usia Anda {usia + 1} tahun.")
```

>**Peringatan:** Jika lupa mengonversi `input()` ke `int`/`float`, operasi matematika akan menghasilkan error atau penggabungan string.

---

## 3. Contoh Program Lengkap

### Studi Kasus: Program Struk Belanja Sederhana
```python
# Program: Hitung Total Belanja dengan Format Rapi
nama_barang = input("Nama barang: ")
harga = float(input("Harga satuan (Rp): "))
jumlah = int(input("Jumlah: "))

total = harga * jumlah

print("\n=== STRUK BELANJA ===")
print(f"Barang  : {nama_barang}")
print(f"Harga   : Rp {harga:,.2f}")
print(f"Jumlah  : {jumlah}")
print(f"Total   : Rp {total:,.2f}")
```

### 🔍 Penjelasan Fitur:
- `float()` & `int()` digunakan karena `input()` selalu mengembalikan string.
- `f-string` (`f"..."`) memungkinkan penyisipan variabel langsung ke dalam string.
- `:,.2f` → format angka: 
  - `,` = pemisah ribuan
  - `.2f` = 2 angka desimal

---

## Quick Reference

```python
# Deklarasi Variabel
x = 10                  # int
y = 3.14                # float
nama = "Alka"           # str
is_active = True        # bool

# Type Casting
angka_str = "100"
angka_int = int(angka_str)      # "100" → 100
angka_float = float("3.14")     # "3.14" → 3.14
teks = str(42)                  # 42 → "42"

# Input & Output
user_input = input("Prompt: ")  # Selalu str!
print(f"Hasil: {user_input}")   # f-string formatting

# Cek Tipe Data
print(type(x))                  # <class 'int'>
```

---

## Common Pitfalls & Solusi

| Masalah | Penyebab | Solusi |
|---------|----------|--------|
| `TypeError: can't multiply sequence by non-int` | Input tidak di-casting ke `int`/`float` | Gunakan `int(input())` atau `float(input())` |
| `NameError: name 'x' is not defined` | Variabel belum dideklarasikan | Pastikan variabel di-assign sebelum digunakan |
| Hasil `10 + 5 = "105"` | Input string digabung, bukan dijumlahkan | Konversi ke angka sebelum operasi matematika |
| Variabel tidak terbaca | Salah penulisan (case-sensitive) | Perhatikan huruf besar/kecil: `Nama` ≠ `nama` |