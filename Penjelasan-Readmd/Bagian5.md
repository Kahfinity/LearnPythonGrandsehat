# Day 5: Loops & Iteration in Python

> **Panduan: Mengotomatisasi Tugas dengan Perulangan yang Efisien**  
> *Loops adalah jantung otomatisasi. Daripada menulis kode berulang, biarkan komputer yang bekerja.*

---

## 1. Konsep Dasar Loops di Python

Python menyediakan dua mekanisme perulangan utama: `for` (deterministik) dan `while` (kondisional).

### `for` Loop (Perulangan Terbatas)
Digunakan ketika jumlah iterasi diketahui atau saat melakukan iterasi melalui koleksi data (`list`, `str`, `tuple`, `range`).

```python
for item in sequence:
    # Blok kode yang diulang
    print(item)
```

### `while` Loop (Perulangan Bersyarat)
Digunakan ketika perulangan berlanjut **selama kondisi bernilai `True`**. Wajib ada mekanisme update kondisi untuk mencegah *infinite loop*.

```python
while kondisi:
    # Blok kode yang diulang
    update_kondisi()  # PENTING: agar loop dapat terminasi
```

### Fungsi `range()`
Generator angka yang hemat memori (tidak menyimpan seluruh list di RAM).  
Sintaks: `range(start, stop, step)`

| Kode | Hasil | Penjelasan |
|------|-------|------------|
| `range(5)` | `0, 1, 2, 3, 4` | Mulai 0, berhenti sebelum 5 |
| `range(2, 6)` | `2, 3, 4, 5` | Mulai 2, berhenti sebelum 6 |
| `range(0, 10, 2)` | `0, 2, 4, 6, 8` | Loncat 2 |
| `range(5, 0, -1)` | `5, 4, 3, 2, 1` | Hitung mundur |

---

## 2. Kontrol Perulangan

| Statement | Fungsi | Analogi |
|-----------|--------|---------|
| `break` | Menghentikan loop sepenuhnya | `"Cukup, keluar sekarang!"` |
| `continue` | Melewati sisa kode iterasi ini, lanjut ke iterasi berikutnya | `"Skip ini, lanjut yang berikutnya"` |
| `pass` | Placeholder (tidak melakukan apa-apa) | `"Nanti saja diisi"` |

```python
for i in range(1, 6):
    if i == 3:
        continue  # Skip angka 3
    if i == 5:
        break     # Berhenti di 5
    print(i, end=" ")  # Output: 1 2 4
```

---

## 3. Contoh Program

### Studi Kasus: `Sistem Login dengan Batas Percobaan & Riwayat`
```python
# Program: Simulasi Login Aman dengan Rate-Limiting Sederhana
password_benar = "python123"
maksimal_percobaan = 3
percobaan = 0
login_berhasil = False

print("SISTEM LOGIN AMAN")

# While Loop: Validasi berkelanjutan dengan batas aman
while percobaan < maksimal_percobaan and not login_berhasil:
    input_user = input(f"Percobaan {percobaan + 1}/{maksimal_percobaan}: Masukkan password: ")
    
    if input_user == password_benar:
        login_berhasil = True
        print("Login Berhasil!")
    else:
        print("Password Salah.")
        percobaan += 1 

if not login_berhasil:
    print("\nAkses Ditolak. Anda telah mencapai batas percobaan.")
else:
    print("\n=== MENU UTAMA ===")
    print("1. Profil")
    print("2. Pengaturan")
    print("3. Keluar")
```
**Apa yang Dipelajari?**
- `while` untuk validasi berkelanjutan + flag boolean
- `for` + `enumerate()` untuk iterasi list dengan counter
- Counter update eksplisit (`percobaan += 1`) → mencegah infinite loop

---