Kode: Sistem Pelayanan Pelanggan (Booking System Sederhana)
---

## Penjelasan

- 🔵 **Nama Fungsi/Kode** → Apa tugasnya?
- 🟡 **Analogi** → Bagaimana cara kerjanya di dunia nyata?
- 🟢 **Konsep Python** → Materi hari ke berapa yang diterapkan?
- 🔴 **Catatan Penting** → Jaga-jaga agar tidak bingung atau terjadi bug.

---

### 1. Bagian Import (Persiapan Peralatan)
```python
import random
from datetime import datetime
```
- `import random`: Memanggil modul acak. *(Catatan: Di versi terbaru kode ini sebenarnya sudah tidak dipakai karena ID dibuat berurutan. Baris ini bisa dihapus tanpa error.)*
- `from datetime import datetime`: Mengambil "kalender & jam digital" bawaan Python. Dipakai untuk memvalidasi format & keberadaan tanggal/jam.
- 🟢 **Day 4**: Memahami `import` seperti meminjam alat dari gudang standar Python.

---

### 2. Fungsi Validasi Tanggal & Jam
```python
def validasi_tanggal(input_tanggal):
    try:
        datetime.strptime(input_tanggal, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def validasi_jam(input_jam):
    try:
        datetime.strptime(input_jam, "%H:%M")
        return True
    except ValueError:
        return False
```
- **Tugas**: Mengecek apakah teks yang diketik user benar-benar berbentuk tanggal/jam yang valid.
- **Cara Kerja**:
  - `datetime.strptime()` = *string parse time*. Python mencoba menerjemahkan teks menjadi objek tanggal/jam.
  - `try:` = "Coba lakukan ini dulu".
  - `except ValueError:` = "Kalau gagal (format salah atau tanggal tidak ada di kalender), tangkap errornya".
  - `return True/False` = Memberi lampu hijau/merah ke pemanggil fungsi.
- 🟡 **Analogi**: Mesin pemindai tiket. Format & tanggal sesuai → mesin nyala hijau (`True`). Tidak sesuai → tolak (`False`).
- 🟢 **Day 2 & 7**: Tipe data string, `try-except` (penanganan error), `return`.

---

### 3. Fungsi Cek Bentrok (Pemeriksa Jadwal)
```python
def cek_bentrok(daftar_booking, tanggal_baru, jam_baru, layanan_baru):
    for booking in daftar_booking:
        if (booking["tanggal"] == tanggal_baru and 
            booking["jam"] == jam_baru and 
            booking["layanan"] == layanan_baru):
            return True
    return False
```
- **Tugas**: Memastikan tidak ada pemesanan ganda untuk **layanan yang sama** di **waktu yang sama**.
- **Cara Kerja**:
  - `for booking in daftar_booking:` = Menelusuri satu per satu data yang sudah tersimpan.
  - `if ... and ... and ...:` = Mengecek 3 kondisi sekaligus. Hanya jika ketiganya cocok, dianggap bentrok.
  - `return True` = Langsung berhenti & beri tahu `"ADA BENTROK"`.
  - `return False` = Jika selesai mengecek semua data & tidak ada yang cocok, beri tahu `"AMAN"`.
- 🟡 **Analogi**: Resepsionis membuka buku agenda. Membolak-balik halaman. Jika menemukan tanggal, jam, & layanan yang persis sama → `"Sudah terisi"`. Jika tidak → `"Bisa booking"`.
- 🟢 **Day 4 & 5**: `list`, `for loop`, akses dictionary (`booking["tanggal"]`), operator logika.

---

### 4. Fungsi Pesan Layanan (Proses Utama)
```python
def pesan_layanan(daftar_booking):
    print("\n--- PEMESANAN LAYANAN BARU ---")
    
    nama = input("Nama Pelanggan: ").strip()
    if not nama:
        print("Nama tidak boleh kosong!")
        return
```
- `input(...).strip()` = Menerima teks, lalu `.strip()` menghapus spasi di awal/akhir yang tidak sengaja diketik.
- `if not nama:` = Jika kosong, tolak & `return` (keluar dari fungsi ini segera).

```python
    print("\nPilih Jenis Layanan:")
    print("1. Konsultasi Teknis")
    print("2. Perbaikan Perangkat")
    print("3. Instalasi & Konfigurasi")
    
    pilihan = input("Masukkan nomor layanan (1-3): ")
    layanan_map = {
        "1": "Konsultasi Teknis",
        "2": "Perbaikan Perangkat",
        "3": "Instalasi & Konfigurasi"
    }
    
    if pilihan not in layanan_map:
        print("Pilihan layanan tidak valid!")
        return
```
- `layanan_map` = **Dictionary**. Mengubah angka `"1"` menjadi teks seragam `"Konsultasi Teknis"`.
- `if pilihan not in layanan_map:` = Validasi menu. Jika user ketik `"4"` atau `"abc"`, proses dibatalkan.

```python
    layanan_dipilih = layanan_map[pilihan]

    while True:
        tanggal = input("Tanggal Layanan (DD/MM/YYYY): ").strip()
        if validasi_tanggal(tanggal):
            break
        print("Format/tanggal salah. Contoh: 12/11/2024")

    while True:
        jam = input("Jam Layanan (HH:MM, 24 jam): ").strip()
        if validasi_jam(jam):
            break
        print("Format jam salah. Contoh: 14:30")
```
- `while True:` = Loop tanpa henti **sampai** kondisi di dalam terpenuhi.
- `if validasi_...(): break` = Jika fungsi validasi memberi lampu hijau (`True`), `break` menghentikan loop. Jika tidak, cetak peringatan & loop berulang.

```python
    if cek_bentrok(daftar_booking, tanggal, jam, layanan_dipilih):
        print(f"Layanan '{layanan_dipilih}' pada {tanggal} jam {jam} SUDAH DIPESAN! Pilih waktu lain.")
        return
```
- Memanggil fungsi `cek_bentrok`. Jika `True`, tampilkan pesan & `return` (batalkan proses, jangan simpan).

```python
    nomor_urut = len(daftar_booking) + 1
    booking_id = f"SRV-{nomor_urut:04d}"

    data_booking = {
        "urutan": nomor_urut,
        "id": booking_id,
        "nama": nama,
        "layanan": layanan_dipilih,
        "tanggal": tanggal,
        "jam": jam
    }
    daftar_booking.append(data_booking)
```
- `len(daftar_booking) + 1` = Menghitung jumlah data + 1 → jadi nomor urut otomatis.
- `f"SRV-{nomor_urut:04d}"` = **f-string formatting**. `:04d` artinya `"angka desimal, selalu 4 digit, kalau kurang tambah 0 di depan"`. Contoh: `1` → `0001`.
- `data_booking = {...}` = **Dictionary**. Mengelompokkan semua informasi jadi 1 `"kartu data"`.
- `daftar_booking.append(data_booking)` = Memasukkan kartu data ke dalam `"lemari"` (`list`).

```python
    print(f"\nBooking berhasil!")
    print(f"No. Urut    : {nomor_urut}")
    print(f"ID          : {booking_id}")
    print(f"Layanan     : {layanan_dipilih}")
    print(f"Tanggal     : {tanggal}")
    print(f"Jam         : {jam}")
```
- Konfirmasi ke user. Menggunakan `f-string` agar variabel langsung tampil di teks secara rapi.

---

### 5. Fungsi Lihat Booking (Laporan/Tabel)
```python
def lihat_booking(daftar_booking):
    print("\n--- DAFTAR BOOKING ---")
    if not daftar_booking:
        print("Belum ada data booking.")
        return
```
- Cek apakah `list` masih kosong. Jika ya, beri tahu & keluar fungsi.

```python
    print(f"{'No.':<4} | {'ID':<8} | {'Nama':<15} | {'Layanan':<25} | {'Tanggal':<12} | {'Jam':<5}")
    print("-" * 80)
    
    for b in daftar_booking:
        print(f"{b['urutan']:<4} | {b['id']:<8} | {b['nama']:<15} | {b['layanan']:<25} | {b['tanggal']:<12} | {b['jam']:<5}")
```
- `{'No.':<4}` = **Alignment**. `<` artinya rata kiri, `4` artinya sediakan 4 karakter. Ini seperti `"penggaris tak terlihat"` agar tabel rapi.
- `"-" * 80` = Mengulang karakter `-` sebanyak 80x (garis pemisah).
- `for b in daftar_booking:` = Mengambil setiap `"kartu data"`, lalu mencetak isinya sesuai kolom yang sudah diatur lebarnya.
- 🟢 **Day 2 & 5**: Manipulasi string, `for loop`, akses dictionary.

---

### 6. Fungsi `main()` & Entry Point (Pengendali Utama)
```python
def main():
    daftar_booking = []
    print("Selamat Datang di Sistem Pelayanan Pelanggan!")
    
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Pesan Layanan Baru")
        print("2. Lihat Daftar Booking")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == "1":
            pesan_layanan(daftar_booking)
        elif pilihan == "2":
            lihat_booking(daftar_booking)
        elif pilihan == "3":
            print("Terima kasih! Program ditutup.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
```
- `daftar_booking = []` = Membuat `"lemari kosong"` yang akan diisi selama program berjalan.
- `while True:` = Menu utama yang terus berputar sampai user memilih `3`.
- `if/elif/else` = **Router**. Mengarahkan user ke fungsi yang sesuai.
- `break` = Memutus `while True`, sehingga program berhenti dengan rapi.
- 🟢 **Day 3 & 5**: Control flow, loop, fungsi.

```python
if __name__ == "__main__":
    main()
```
- **Apa ini?**: `"Jika file ini dijalankan langsung (bukan di-impor oleh file lain), maka jalankan main()"`.
- Praktik standar Python agar kode tidak jalan otomatis saat kita hanya ingin meminjam fungsinya di proyek lain.

---

## Ringkasan Konsep

| Konsep | Analogi Cepat | Di Kode Mana? |
|--------|--------------|---------------|
| `try-except` | Jaring pengaman saat input salah | `validasi_tanggal/jam` |
| `while True + break` | `"Ulangi sampai benar"` | Loop validasi tanggal/jam |
| `dictionary` | Kartu data terorganisir | `data_booking = {...}` |
| `list of dict` | Lemari berisi kartu-kartu | `daftar_booking` |
| `f-string alignment` | Penggaris otomatis untuk tabel | `lihat_booking()` |
| `return` awal | `"Batalkan proses, keluar dari fungsi"` | Saat input kosong/bentrok |

---