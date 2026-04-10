while True:
    print("\n=== MENU === ")
    print("1. Cek Bilangan")
    print("2. Keluar")

    pilihan = input("Pilih menu (1/2): ")

    if pilihan == '1':
        try:
            angka = int(input("Masukkan bilangan: "))

            if angka == 0:
                print("Bilangan tersebut adalah Nol")
            elif angka % 2 == 0:
                print(f"{angka} adalah bilangan Genap")
            else:
                print(f"{angka} adalah bilangan Ganjil")
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")

    elif pilihan == '2':
        print("Terima kasih! Keluar dari program...")
        break
    else:
        print("Pilihan tidak tersedia. Silakan coba lagi.")