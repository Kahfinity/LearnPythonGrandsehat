import random  # 1. Mengimpor modul random untuk mengacak angka


def main():
    print("=== Selamat Datang di Game Tebak Angka ===")
    print("Saya sedang memikirkan sebuah angka antara 1 sampai 10.")

    # 2. Komputer memilih angka rahasia secara acak
    angka_rahasia = random.randint(1, 10)

    kesempatan = 3  # 3. Batas jumlah tebakan
    tebakan = 0  # 4. Variabel untuk menyimpan tebakan pemain

    # 5. Perulangan while: Game berjalan selama kesempatan masih ada
    # dan pemain belum menebak angka yang benar
    while kesempatan > 0 and tebakan != angka_rahasia:
        print(f"\nKesempatan tersisa: {kesempatan}")

        # 6. Meminta input dari user
        # input() selalu menghasilkan teks (string), jadi kita ubah ke angka (int)
        try:
            tebakan = int(input("Masukkan tebakan Anda (1-10): "))
        except ValueError:
            print("⚠️  Harap masukkan angka yang valid!")
            continue  # Lewati sisa loop dan ulang ke awal loop

        # 7. Logika Percabangan (If/Else)
        if tebakan < angka_rahasia:
            print("Terlalu rendah! Coba lagi.")
        elif tebakan > angka_rahasia:
            print("Terlalu tinggi! Coba lagi.")
        else:
            print(f"SELAMAT! Anda benar. Angkanya adalah {angka_rahasia}.")

        # 8. Mengurangi kesempatan setiap kali menebak (jika salah)
        if tebakan != angka_rahasia:
            kesempatan -= 1

    # 9. Pesan jika kesempatan habis
    if kesempatan == 0 and tebakan != angka_rahasia:
        print(f"\nYah, kesempatan habis. Angka rahasianya adalah {angka_rahasia}.")


# 10. Menjalankan fungsi main
if __name__ == "__main__":
    main()