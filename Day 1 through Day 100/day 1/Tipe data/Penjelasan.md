**1. Tipe Data Numerik (Angka)
Digunakan untuk operasi matematika.**

    int (Integer): Bilangan bulat.
    float: Bilangan desimal (menggunakan titik).
    complex: Bilangan kompleks (jarang digunakan untuk pemula, tapi ada).

Penjelasan Fungsi Code:
Kode di atas menyimpan nilai angka ke dalam variabel. Fungsi type() digunakan untuk memeriksa jenis data apa yang sebenarnya disimpan oleh variabel tersebut.

**3. Tipe Data Sequence (Urutan)
Digunakan untuk menyimpan kumpulan data.**

    str (String): Kumpulan karakter (teks).
    list: Kumpulan data terurut, bisa diubah (mutable), menggunakan kurung siku [].
    tuple: Kumpulan data terurut, tidak bisa diubah (immutable), menggunakan kurung biasa ().

Penjelasan Fungsi Code:
Kode ini menunjukkan cara menyimpan teks dan kumpulan data. Pada list, kita menggunakan metode .append() untuk menambah data baru. Pada string, kita bisa mengakses karakter spesifik menggunakan indeks (dimulai dari 0).

**4. Tipe Data Mapping (Pemetaan)**

    dict (Dictionary): Menyimpan data dalam pasangan Key : Value (Kunci : Nilai). Sangat berguna untuk data terstruktur.

Penjelasan Fungsi Code:
Kita membuat data terstruktur seperti kamus. Untuk mengakses nilainya, kita memanggil key-nya (contoh: "nama"). Ini lebih efisien daripada menggunakan indeks angka seperti pada list.

**5. Tipe Data Boolean & None**

    bool: Hanya memiliki dua nilai, True atau False. Digunakan untuk logika percabangan.
    NoneType: Mewakili ketiadaan nilai (kosong).

Penjelasan Fungsi Code:
Variabel is_active digunakan dalam pernyataan if untuk menentukan apakah kode di dalamnya harus dijalankan. None sering digunakan sebagai nilai default ketika sebuah variabel belum memiliki isi yang valid.

**6. Tipe Data Set (Himpunan)**

    set: Kumpulan data unik (tidak ada duplikat) dan tidak terurut.

Penjelasan Fungsi Code:
Kode ini menunjukkan keunggulan utama set, yaitu otomatis menghilangkan data yang sama (duplikat). Ini berguna jika Anda hanya membutuhkan daftar nilai unik.