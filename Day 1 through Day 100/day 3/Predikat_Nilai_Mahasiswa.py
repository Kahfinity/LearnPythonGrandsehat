uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))
tugas = float(input("Nilai Tugas: "))

# Validasi range
if not (0 <= uts <= 100 and 0 <= uas <= 100 and 0 <= tugas <= 100):
    print("Input tidak valid. Nilai harus antara 0-100.")
else:
    akhir = (0.3 * uts) + (0.5 * uas) + (0.2 * tugas)

    if akhir >= 85:
        predikat = "A"
    elif akhir >= 70:
        predikat = "B"
    elif akhir >= 55:
        predikat = "C"
    elif akhir >= 40:
        predikat = "D"
    else:
        predikat = "E"

    print(f"\nNilai Akhir: {akhir:.2f}")
    print(f"Predikat   : {predikat}")