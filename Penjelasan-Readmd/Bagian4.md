# Day 4: Randomization & Python Lists

> **Panduan: Membuat Program Dinamis dengan Data Terstruktur & Acak**  
> *Kombinasi randomisasi + list membuka pintu ke game, simulasi, pengolah data, dan aplikasi interaktif*

---

## 1. Randomisasi di Python

Python menyediakan modul bawaan `random` untuk menghasilkan nilai acak (*pseudo-random*). Cocok untuk game, simulasi, atau pengujian.

### Fungsi-Fungsi Utama Modul `random`

| Fungsi | Deskripsi | Contoh | Hasil |
|--------|-----------|--------|-------|
| `randint(a, b)` | Integer acak antara `a` dan `b` **(inklusif)** | `randint(1, 6)` | `4` |
| `random()` | Float antara `0.0` dan `1.0` | `random()` | `0.732...` |
| `choice(seq)` | Pilih **1 elemen acak** dari list/string/tuple | `choice(["A","B"])` | `"B"` |
| `shuffle(list)` | **Mengacak urutan list secara in-place** | `shuffle(lst)` | `lst` berubah |
| `sample(pop,k)` | Ambil `k` elemen unik secara acak | `sample([1,2,3,4], 2)` | `[3, 1]` |

### ⚠️ Catatan Penting
```python
import random

# shuffle() & sort() mengembalikan None (in-place operation)
lst = [1, 2, 3]
result = random.shuffle(lst)
print(result)  # None! List lst yang berubah, bukan result

# random adalah pseudo-random → JANGAN untuk keamanan
# modul `secrets` untuk token, password, atau data sensitif
import secrets
token = secrets.token_hex(16)
```


> - `random` → cocok untuk game, simulasi, testing  
> - `secrets` → wajib untuk token auth, password reset, API keys  
> - Jangan pernah gunakan `random` untuk data sensitif!

---

## 2. Python Lists: Konsep & Operasi Dasar

List adalah **kumpulan terurut yang bisa diubah (`mutable`)**. Berbeda dengan string, elemen list bisa ditambah, dihapus, atau diganti.

### Pembuatan & Indexing
```python
buah = ["apel", "mangga", "jeruk", "anggur"]

# Indexing positif (dari kiri, mulai 0)
print(buah[0])    # "apel"
print(buah[2])    # "jeruk"

# Indexing negatif (dari kanan, mulai -1)
print(buah[-1])   # "anggur"
print(buah[-2])   # "jeruk"

# Slicing [start:stop:step] → stop eksklusif
print(buah[1:3])  # ["mangga", "jeruk"]
print(buah[:2])   # ["apel", "mangga"]
print(buah[::2])  # ["apel", "jeruk"] → loncat 2
```

### Metode List Paling Sering Dipakai

| Metode | Fungsi | Return Value | Catatan |
|--------|--------|-------------|---------|
| `.append(x)` | Tambah `x` di akhir | `None` | In-place |
| `.insert(i,x)` | Sisipkan `x` di indeks `i` | `None` | Geser elemen ke kanan |
| `.remove(x)` | Hapus **kemunculan pertama** `x` | `None` | `ValueError` jika tidak ada |
| `.pop([i])` | Hapus & kembalikan elemen di `i` | `elemen` | Default: indeks terakhir |
| `.sort()` | Urutkan menaik (in-place) | `None` | Homogen tipe disarankan |
| `.reverse()` | Balik urutan (in-place) | `None` | Tidak mengurutkan |
| `len(list)` | Jumlah elemen | `int` | Fungsi bawaan, bukan metode |
| `x in list` | Cek keberadaan | `bool` | Linear search O(n) |

---

## 3. Contoh Program

### Studi Kasus: `Pemilih Aktivitas Harian & Riwayat`
```python
import random

# Data awal
aktivitas = ["Olahraga", "Baca Buku", "Coding", "Meditasi", "Menonton"]
riwayat = []

# 1. Pilih aktivitas acak untuk hari ini
pilihan = random.choice(aktivitas)

# 2. Tampilkan & simpan ke riwayat
print(f"Aktivitas hari ini: {pilihan}")
riwayat.append(pilihan)  # append() return None, langsung panggil tanpa assignment

# 3. Acak urutan & tampilkan 3 rekomendasi
random.shuffle(aktivitas)  # shuffle() mengubah list asli
print("\n3 Rekomendasi Minggu Ini:")
for i in range(3):
    print(f"  {i+1}. {aktivitas[i]}")

# 4. Tampilkan riwayat
print(f"\nRiwayat hari ini: {riwayat}")
```

### Apa yang Dipelajari?
| Konsep | Implementasi |
|--------|-------------|
| `random.choice()` | Pilih 1 elemen acak dari list |
| `list.append()` | Tambah elemen ke akhir list |
| `random.shuffle()` | Acak urutan list in-place |
| `for + range()` | Iterasi sederhana dengan counter |
---