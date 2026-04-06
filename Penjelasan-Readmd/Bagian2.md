# Day 2: Deep Dive into Data Types & String Manipulation

> *String adalah tipe data paling sering dijumpai di dunia nyata (input user, file, API, database)*

---

## 1. Tipe Data Python: Review & Ekspansi

Python adalah bahasa *dynamically typed*. Anda tidak perlu mendeklarasikan tipe, tetapi Python tetap menyimpan tipe data.

| Tipe | Deskripsi | Contoh | Catatan Penting |
|------|-----------|--------|----------------|
| `int` | Bilangan bulat | `42`, `-7`, `0` | Tidak ada batas ukuran (hanya terbatas RAM) |
| `float` | Bilangan desimal | `3.14`, `2.0`, `-0.5` | Presisi terbatas (~15 digit desimal) |
| `str` | Urutan karakter | `"Halo"`, `'123'`, `""` | **Immutable** (tidak bisa diubah) |
| `bool` | Nilai logika | `True`, `False` | `1` ≈ `True`, `0` ≈ `False` dalam konteks boolean |
| `None` | Ketidakadaan nilai | `None` | Bukan `0`, bukan `""`, bukan `False` |

>**Cek Tipe Data:** `type(variabel)`  
>**Konversi Tipe:** `int()`, `float()`, `str()`, `bool()`  
>`None` tidak bisa dikonversi langsung ke numerik → akan menyebabkan `TypeError`

---

## 2. Karakteristik String di Python

### Immutability (Tidak Bisa Diubah)
```python
teks = "Python"
# teks[0] = "J"  ❌ TypeError: 'str' object does not support item assignment

# ✅ Solusi: Buat string baru
teks = "J" + teks[1:]  # "Jython"
```

### Indexing (Pengambilan Karakter)
- Index dimulai dari `0` (kiri) atau `-1` (kanan)
```python
kata = "PYTHON"
print(kata[0])    # P
print(kata[-1])   # N
print(kata[2])    # T
print(kata[-3])   # H
```

### Slicing (Pemotongan String)
**Sintaks:** `string[start:stop:step]`
- `stop` bersifat **eksklusif** (tidak termasuk)
- `step` opsional (default `1`)

```python
teks = "0123456789"
print(teks[2:5])     # "234" → indeks 2,3,4
print(teks[:4])      # "0123" → dari awal sampai indeks 3
print(teks[5:])      # "56789" → dari indeks 5 sampai akhir
print(teks[::2])     # "02468" → loncat 2 karakter
print(teks[::-1])    # "9876543210" → membalik string
print(teks[-4:-1])   # "678" → slicing dengan indeks negatif
```

### Escape Characters
| Simbol | Arti | Contoh Output |
|--------|------|--------------|
| `\n` | Baris baru (newline) | `Baris1\nBaris2` → 2 baris |
| `\t` | Tab horizontal | `Nama:\tAl` → `Nama:   Al` |
| `\\` | Backslash literal | `C:\\Users` → `C:\Users` |
| `\"` atau `\'` | Quotes dalam string | `"Kata \"Spesial\""` → `Kata "Spesial"` |

```python
print("Baris 1\nBaris 2\t[Terinduk]")
# Output:
# Baris 1
# Baris 2 [Terinduk]

print("Kata \"Spesial\" di sini")  # Output: Kata "Spesial" di sini
```

---

## 3. Metode String Paling Berguna (Cheat Sheet)

String di Python punya puluhan metode bawaan :

| Metode | Fungsi | Contoh | Hasil |
|--------|--------|--------|-------|
| `.upper()` / `.lower()` | Ubah ke huruf besar/kecil | `"Py".upper()` | `"PY"` |
| `.strip()` | Hapus whitespace di awal/akhir | `"  hi  ".strip()` | `"hi"` |
| `.replace(old, new)` | Ganti substring | `"a-b".replace("-", "_")` | `"a_b"` |
| `.split(sep)` | Pecah string jadi list | `"a,b,c".split(",")` | `['a','b','c']` |
| `sep.join(list)` | Gabung list jadi string | `",".join(['a','b'])` | `"a,b"` |
| `.find(sub)` | Cari indeks pertama substring | `"abc".find("b")` | `1` (jika tidak ada → `-1`) |
| `.count(sub)` | Hitung kemunculan substring | `"banana".count("a")` | `3` |
| `.startswith()` / `.endswith()` | Cek awalan/akhiran | `"file.py".endswith(".py")` | `True` |
| `.isalpha()` / `.isdigit()` | Cek jenis karakter | `"123".isdigit()` | `True` |
| `.title()` / `.capitalize()` | Format kapitalisasi | `"hello world".title()` | `"Hello World"` |

> **Note:** Selalu sanitasi input user sebelum diproses lebih lanjut. Gunakan `.strip()` dan validasi tipe untuk mencegah error tak terduga.

---

## 4. String Formatting Modern (f-string)

**Rekomendasi Python 3.6+** — lebih cepat dan mudah dibaca.

```python
nama = "Budi"
skor = 95.7
level = 5

# Basic f-string
print(f"Selamat {nama}, skor Anda {skor:.1f}!")  
# Output: Selamat Budi, skor Anda 95.7!

# Alignment & padding
print(f"{'Kiri':<10}|{'Tengah':^10}|{'Kanan':>10}|")
# Output: Kiri      |  Tengah  |     Kanan|

# Format angka & persentase
print(f"Level: {level:03d} | Akurasi: {skor:.0%}")  
# Output: Level: 005 | Akurasi: 96%

# Ekspresi di dalam f-string
print(f"{nama.upper()} memiliki {len(nama)} karakter")
# Output: BUDI memiliki 4 karakter
```