total = float(input("Total belanja (Rp): "))
kode = input("Kode member: ").strip().lower()

diskon_persen = 0

if total >= 500000:
    diskon_persen = 20
elif total >= 200000:
    diskon_persen = 10

if kode == "gold":
    diskon_persen += 5  # Tambahan 5% bisa di-stack

total_diskon = total * (diskon_persen / 100)
bayar = total - total_diskon

print(f"\nDiskon: {diskon_persen}%")
print(f"Potongan: Rp {total_diskon:,.0f}")
print(f"Total Bayar: Rp {bayar:,.0f}")