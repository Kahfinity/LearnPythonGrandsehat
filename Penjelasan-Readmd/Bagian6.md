# Day 6: Functions & Modular Programming (Karel Philosophy)

> **Panduan: Mengorganisir Kode dengan Fungsi & Prinsip Dekomposisi**  
> *Jika variabel adalah wadah dan loop adalah otot, fungsi adalah otak yang mengatur logika. Tulis sekali, gunakan berkali-kali, hindari bug berulang.*

---

## 1. Apa Itu Fungsi (Function)?
Fungsi adalah **blok kode terisolasi yang dapat dipanggil kembali** untuk menjalankan tugas spesifik.

### Mengapa Menggunakan Fungsi?
| Tanpa Fungsi | Dengan Fungsi |
|--------------|---------------|
| Kode berulang (Copy-Paste) | Tulis sekali, eksekusi berkali-kali |
| Sulit dibaca, diuji, & dipelihara | Terstruktur, modular, & mudah di-debug |
| Bug harus diperbaiki di banyak tempat | Perbaikan cukup di satu definisi fungsi |

### Sintaks Dasar
```python
def nama_fungsi():
    # Blok kode yang dijalankan
    print("Halo dari fungsi!")

# Memanggil fungsi (eksekusi hanya terjadi saat dipanggil)
nama_fungsi()
```
**Aturan:** `def` → definisi, `()` → placeholder parameter, `:` → awal blok.

---

## 2. Parameter, Argumen, & Return
### Parameter vs Argumen
| Istilah | Definisi | Contoh |
|---------|----------|--------|
| **Parameter** | Variabel placeholder di definisi `def` | `def sapa(nama):` |
| **Argumen** | Nilai nyata yang dikirim saat pemanggilan | `sapa("Budi")` |

### `return` vs `print`
| Fitur | Fungsi | Hasil |
|-------|--------|-------|
| `print()` | Menampilkan ke console | Tidak mengembalikan nilai (`None`) |
| `return` | Mengembalikan data ke pemanggil | Bisa disimpan, diproses, atau diteruskan |

```python
def tambah_print(a, b):
    print(a + b)  # Hanya tampil di layar

def tambah_return(a, b):
    return a + b  # Mengembalikan nilai

hasil = tambah_return(5, 3)  #hasil = 8
# hasil = tambah_print(5, 3)  #hasil = None (print tidak mengembalikan data)
```
> Gunakan `return` untuk logika bisnis/pemrosesan data. Gunakan `print()` hanya untuk output akhir atau debugging.

---

## 3. Filosofi Karel: Decomposition & Abstraction
Karel adalah robot edukasi yang hanya memahami perintah primitif. Untuk tugas kompleks, kita **memecah masalah** menjadi fungsi kecil (*decomposition*), lalu menyusunnya menjadi alur yang lebih tinggi (*abstraction*).

**Contoh Pola Karel dalam Python:**
```python
# Primitif (disediakan oleh sistem)
def belok_kiri(): pass
def maju(): pass
def ambil_benda(): pass

# Dekomposisi: Fungsi komposit dari primitif
def belok_kanan():
    """Karel hanya bisa belok kiri, kanan = 3x kiri"""
    belok_kiri()
    belok_kiri()
    belok_kiri()

def jalan_satu_langkah():
    maju()
    ambil_benda()

# Abstraksi: Logika tingkat tinggi
def bersihkan_ruangan():
    for _ in range(5):
        jalan_satu_langkah()
```
---

## 4. Scope & State Management
Scope menentukan di mana variabel dapat diakses.

| Scope | Deskripsi | Akses |
|-------|-----------|-------|
| **Local** | Dibuat di dalam fungsi | Hanya di dalam fungsi tersebut |
| **Global** | Dibuat di luar fungsi | Bisa dibaca di mana saja, tapi **hindari modifikasi di dalam fungsi** |

```python
x = 10  # Global

def demo_scope():
    y = 5  # Local
    print(x)  # Baca global
    print(y)  # Baca local

demo_scope()
# print(y)  # NameError: y tidak terdefinisi di scope global
```
---

## 5. Contoh Program Terpadu

### Studi Kasus: `Simulasi Robot Karel Text-Based`
```python
# --- Fungsi Dasar (Primitive) ---
def maju(posisi: int) -> int:
    """Menaikkan posisi robot sebesar 1"""
    return posisi + 1

def mundur(posisi: int) -> int:
    """Menurunkan posisi robot sebesar 1"""
    return posisi - 1

# --- Fungsi Komposit (Abstraksi) ---
def gerak_maju_2_langkah(posisi_awal: int) -> int:
    """Robot bergerak 2 langkah ke depan"""
    pos = maju(posisi_awal)
    return maju(pos)  # Chaining function call

def putar_balik(posisi: int) -> int:
    """Simulasi putar balik (mundur 2 langkah)"""
    return mundur(mundur(posisi))

# --- Program Utama (Orchestrator) ---
def main():
    lokasi_awal = 0
    print(f"Robot mulai di lokasi: {lokasi_awal}")

    lokasi_sekarang = gerak_maju_2_langkah(lokasi_awal)
    print(f"Setelah 2 langkah maju: {lokasi_sekarang}")

    lokasi_sekarang = putar_balik(lokasi_sekarang)
    print(f"Setelah putar balik: {lokasi_sekarang}")

    if lokasi_sekarang == lokasi_awal:
        print("Robot kembali ke titik awal.")

# Eksekusi hanya jika file dijalankan langsung
if __name__ == "__main__":
    main()
```
**Apa yang Dipelajari?**
-  `return` untuk passing state antar fungsi
- Function chaining & komposisi
- `docstring` & type hints (`: int`, `-> int`) untuk dokumentasi & tooling
- `if __name__ == "__main__":` → standar produksi agar kode aman saat di-import sebagai modul

---