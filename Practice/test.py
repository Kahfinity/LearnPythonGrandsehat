# Program: Simulasi Login Aman dengan Rate-Limiting Sederhana
password_benar = "python123"
maksimal_percobaan = 3
percobaan = 0
login_berhasil = False

print("SISTEM LOGIN AMAN")

# While Loop: Validasi berkelanjutan dengan batas aman
while percobaan < maksimal_percobaan and not login_berhasil:
    input_user = input(f"Percobaan {percobaan + 1}/{maksimal_percobaan} \nMasukkan password: ")

    if input_user == password_benar:
        login_berhasil = True
        print("Login Berhasil!")
    else:
        print("Password Salah.")
        percobaan += 1

if not login_berhasil:
    print("\nAkses Ditolak. Anda telah mencapai batas percobaan.")
else:
    # For Loop: Iterasi menu utama
    menu = ["Profil", "Pengaturan", "Keluar"]
    print("\n=== MENU UTAMA ===")
    print("1. Profil")
    print("2. Pengaturan")
    print("3. Keluar")