print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# Input data pengunjung
nama_3002 = input("Masukkan Nama Pengunjung        : ")
umur_3002 = int(input("Input umur anda                 : "))
sim_3002 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()[0]
jumlah_tiket_3002 = int(input("Masukkan jumlah tiket           : "))

# If tunggal untuk validasi jumlah tiket
if jumlah_tiket_3002 <= 0:
    print("Peringatan: Kuota tiket tidak valid.")

print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

paket_3002 = int(input("Masukkan nomor paket (1-5)      : "))

# Match-case untuk memilih wahana
match paket_3002:
    case 1:
        nama_wahana_3002 = "Wahana Safari Rimba"
        harga_satuan_3002 = 50000

    case 2:
        nama_wahana_3002 = "Wahana Arung Jeram"
        harga_satuan_3002 = 75000

    case 3:
        nama_wahana_3002 = "Wahana Motor ATV Ekstrim"
        harga_satuan_3002 = 120000

    case 4:
        nama_wahana_3002 = "Wahana Roller Coaster Kilat"
        harga_satuan_3002 = 100000

    case 5:
        nama_wahana_3002 = "Wahana All-Access VIP"
        harga_satuan_3002 = 220000

    case _:
        print("Paket wahana tidak valid!")
        exit()

# Input member dan promo
is_member_3002 = input("Apakah Anda member? (y/t)       : ").strip().lower()
kode_promo_valid_3002 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

# Validasi izin wahana
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_3002 == 3:
    if umur_3002 >= 17 and sim_3002 == 'y':
        print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
    elif umur_3002 >= 17 and sim_3002 != 'y':
        print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
    elif umur_3002 < 17 and sim_3002 == 'y':
        print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
    else:
        print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
else:
    if umur_3002 >= 10:
        print("Status Akses: Anda memenuhi syarat umur untuk wahana.")
    else:
        print("Status Akses: Anda belum cukup umur untuk wahana ini.")

# Perhitungan subtotal
subtotal_3002 = harga_satuan_3002 * jumlah_tiket_3002

# Multi-if terpisah untuk diskon akumulatif
total_diskon_persen_3002 = 0

if subtotal_3002 >= 200000:
    total_diskon_persen_3002 += 10

if is_member_3002 in ['y', 'ya']:
    total_diskon_persen_3002 += 5

if kode_promo_valid_3002 in ['y', 'ya']:
    total_diskon_persen_3002 += 15

if jumlah_tiket_3002 >= 5:
    total_diskon_persen_3002 += 5

# Perhitungan pembayaran
nominal_diskon_3002 = subtotal_3002 * (total_diskon_persen_3002 / 100)
total_bayar_3002 = subtotal_3002 - nominal_diskon_3002

# Audit transaksi
if total_bayar_3002 > 300000:
    catatan_layanan_3002 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_3002 = "Terima kasih telah berkunjung."

# Menampilkan rincian
print("\n--- RINCIAN PEMBAYARAN ---")
print(f"Nama Pengunjung  : {nama_3002}")
print(f"Wahana           : {nama_wahana_3002}")
print(f"Subtotal Belanja : Rp {subtotal_3002:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_3002}% (Rp {nominal_diskon_3002:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_3002:,.0f}")
print(f"Catatan Layanan  : {catatan_layanan_3002}")

print("Program Selesai")