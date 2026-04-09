import random
from datetime import datetime


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


def cek_bentrok(daftar_booking, tanggal_baru, jam_baru, layanan_baru):
    """Cek bentrok: hanya blokir jika TANGGAL, JAM, DAN LAYANAN sama persis"""
    for booking in daftar_booking:
        if (booking["tanggal"] == tanggal_baru and
                booking["jam"] == jam_baru and
                booking["layanan"] == layanan_baru):
            return True
    return False


def pesan_layanan(daftar_booking):
    print("\n--- PEMESANAN LAYANAN BARU ---")

    nama = input("Nama Pelanggan: ").strip()
    if not nama:
        print("Nama tidak boleh kosong!")
        return

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

    # Simpan nama layanan yang dipilih SEKARANG agar bisa dipakai di cek_bentrok
    layanan_dipilih = layanan_map[pilihan]

    # Validasi Tanggal
    while True:
        tanggal = input("Tanggal Layanan (DD/MM/YYYY): ").strip()
        if validasi_tanggal(tanggal):
            break
        print("⚠️ Format/tanggal salah. Contoh: 12/11/2024")

    # Validasi Jam
    while True:
        jam = input("Jam Layanan (HH:MM, 24 jam): ").strip()
        if validasi_jam(jam):
            break
        print("Format jam salah. Contoh: 14:30")

    # Cek Bentrok (sekarang termasuk jenis layanan)
    if cek_bentrok(daftar_booking, tanggal, jam, layanan_dipilih):
        print(f"Layanan '{layanan_dipilih}' pada {tanggal} jam {jam} SUDAH DIPESAN! Pilih waktu lain.")
        return

    # Nomor Urut & ID
    nomor_urut = len(daftar_booking) + 1
    booking_id = f"SRV-{nomor_urut:04d}"

    # Simpan data
    data_booking = {
        "urutan": nomor_urut,
        "id": booking_id,
        "nama": nama,
        "layanan": layanan_dipilih,
        "tanggal": tanggal,
        "jam": jam
    }
    daftar_booking.append(data_booking)

    print(f"\nBooking berhasil!")
    print(f"No. Urut    : {nomor_urut}")
    print(f"ID          : {booking_id}")
    print(f"Layanan     : {layanan_dipilih}")
    print(f"Tanggal     : {tanggal}")
    print(f"Jam         : {jam}")


def lihat_booking(daftar_booking):
    print("\n--- DAFTAR BOOKING ---")
    if not daftar_booking:
        print("Belum ada data booking.")
        return

    print(f"{'No.':<4} | {'ID':<8} | {'Nama':<15} | {'Layanan':<25} | {'Tanggal':<12} | {'Jam':<5}")
    print("-" * 80)

    for b in daftar_booking:
        print(
            f"{b['urutan']:<4} | {b['id']:<8} | {b['nama']:<15} | {b['layanan']:<25} | {b['tanggal']:<12} | {b['jam']:<5}")


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


if __name__ == "__main__":
    main()