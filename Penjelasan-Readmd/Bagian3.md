# Day 3: Control Flow & Conditional Logic

> *Tanpa control flow, kode hanya berjalan linear. Dengan `if-elif-else`, program menjadi adaptif dan siap produksi.*

---

## 1. Konsep Control Flow & Operator

### Apa Itu Control Flow?
Control flow adalah **mekanisme yang menentukan urutan eksekusi kode** berdasarkan kondisi tertentu. Di Python, ini dikelola oleh:
- Pernyataan kondisional (`if`/`elif`/`else`)

### Operator Perbandingan (Comparison Operators)
Menghasilkan nilai `bool` (`True`/`False`).

| Operator | Arti | Contoh | Hasil |
|----------|------|--------|-------|
| `==` | Sama dengan | `5 == 5` | `True` |
| `!=` | Tidak sama | `5 != 3` | `True` |
| `>` | Lebih besar | `5 > 3` | `True` |
| `<` | Lebih kecil | `5 < 3` | `False` |
| `>=` | Lebih besar/sama | `5 >= 5` | `True` |
| `<=` | Lebih kecil/sama | `5 <= 3` | `False` |

> **Peringatan Fatal:**  
> - `=` → **penugasan nilai** (assignment)  
> - `==` → **perbandingan** (comparison)

### Operator Logika (Logical Operators)
Menggabungkan beberapa kondisi boolean.

| Operator | Arti | Contoh | Hasil |
|----------|------|--------|-------|
| `and` | Keduanya harus `True` | `True and False` | `False` |
| `or` | Salah satu `True` sudah cukup | `True or False` | `True` |
| `not` | Membalik nilai boolean | `not True` | `False` |

> Python berhenti mengevaluasi begitu hasil sudah pasti:
> - `A and B`: Jika `A` `False` → `B` tidak dicek
> - `A or B`: Jika `A` `True` → `B` tidak dicek  
>   

---

## 2. Struktur `if-elif-else` & Indentasi

Python menggunakan **indentasi (spasi)** untuk menentukan blok kode, bukan kurung kurawal `{}`.

```python
if kondisi_1:
    # Blok 1: dijalankan jika kondisi_1 True
    print("Kondisi 1 terpenuhi")
elif kondisi_2:
    # Blok 2: dijalankan jika kondisi_1 False, tapi kondisi_2 True
    print("Kondisi 2 terpenuhi")
else:
    # Blok 3: dijalankan jika semua kondisi di atas False
    print("Semua kondisi gagal")
```
---

## 3. Contoh Program

### Studi Kasus: `Sistem Klasifikasi Pengguna & Akses`
```python
# Program: Penentuan Level Akses Berdasarkan Usia & Status
# Fokus: input validation, boolean logic, if-elif-else flow

# 1. Input & konversi tipe data
usia = int(input("Masukkan usia Anda: "))
is_member = input("Apakah Anda member? (y/n): ").strip().lower() == "y"
saldo = float(input("Masukkan saldo akun (Rp): "))

# 2. Kontrol alur keputusan dengan prioritas logika
if usia < 13:
    print("Akses Ditolak: Di bawah usia 13 tahun.")
elif usia < 18 and not is_member:
    print("Akses Terbatas: Hanya fitur edukasi. Gabung member untuk akses penuh.")
elif saldo >= 500000 or (usia >= 18 and is_member):
    print("Akses Premium Diberikan. Fitur lengkap aktif.")
else:
    print("Akses Standar. Saldo atau status member perlu ditingkatkan.")

print("\nTerima kasih telah menggunakan sistem kami.")
```

### Apa yang Dipelajari?
| Konsep | Implementasi dalam Kode |
|--------|------------------------|
| Type conversion | `int()`, `float()`, boolean dari string |
| Boolean logic | `and`/`or`/`not` dengan prioritas evaluasi |
| Conditional flow | `if-elif-else` dengan eksekusi eksklusif |
| Input sanitization | `.strip().lower()` untuk normalisasi input |