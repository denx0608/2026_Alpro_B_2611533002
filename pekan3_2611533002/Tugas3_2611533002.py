
# ==========================================
# SISTEM SIMULASI TRANSAKSI TOKO
# Nama: Muhammad Danish Abshori
# NIM: 2611533002
# ==========================================

print("=== SISTEM TRANSAKSI TOKO ===")

# Input data pelanggan
nama_3002 = input("Masukkan Nama Pelanggan : ")
status_3002 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()
total_belanja_3002 = float(input("Masukkan Total Belanja : Rp"))
jumlah_barang_3002 = int(input("Masukkan Jumlah Barang : "))
kode_promo_3002 = input("Masukkan Kode Promo : ").upper()

# Daftar kode promo
daftar_promo_3002 = ["SKIRK08", "FURINA09", "COLOMBINA06"]

# ==========================================
# OPERATOR PERBANDINGAN
# ==========================================

syarat_belanja_3002 = total_belanja_3002 >= 200000
syarat_barang_3002 = jumlah_barang_3002 >= 3
status_member_3002 = status_3002 == "member"

# ==========================================
# OPERATOR KEANGGOTAAN
# ==========================================

promo_tersedia_3002 = kode_promo_3002 in daftar_promo_3002
promo_tidak_tersedia_3002 = kode_promo_3002 not in daftar_promo_3002

# ==========================================
# OPERATOR LOGIKA
# ==========================================

diskon_member_3002 = status_member_3002 and syarat_belanja_3002

# and: harus memenuhi kedua kondisi
promo_3002 = syarat_barang_3002 and promo_tersedia_3002

# or: salah satu kondisi sudah cukup
akses_dasar_3002 = status_member_3002 or syarat_belanja_3002

# not: membalik nilai True menjadi False atau sebaliknya
bukan_member_3002 = not status_member_3002

# ==========================================
# OPERATOR ARITMATIKA
# ==========================================

# Diskon 10% jika member dan belanja minimal Rp200.000
if diskon_member_3002:
    diskon_3002 = total_belanja_3002 * 10 / 100
else:
    diskon_3002 = 0

# Total pembayaran menggunakan operator -
total_pembayaran_3002 = total_belanja_3002 - diskon_3002

# Rata-rata harga barang menggunakan /
rata_rata_3002 = total_belanja_3002 / jumlah_barang_3002

# Sisa pembagian menggunakan %
sisa_3002 = jumlah_barang_3002 % 2

# ==========================================
# OPERATOR PENUGASAN
# ==========================================

poin_3002 = 0

# Operator +=
poin_3002 += jumlah_barang_3002

# Operator -=
saldo_3002 = total_belanja_3002
saldo_3002 -= diskon_3002

# ==========================================
# OPERATOR IDENTITY
# ==========================================

kode_pertama_3002 = kode_promo_3002
kode_kedua_3002 = kode_promo_3002

# is digunakan untuk membandingkan identitas objek
identitas_sama_3002 = kode_pertama_3002 is kode_kedua_3002

# is not digunakan untuk mengecek apakah objek berbeda
identitas_berbeda_3002 = kode_pertama_3002 is not kode_kedua_3002

# ==========================================
# OPERATOR BITWISE
# ==========================================

kode_status_3002 = 0

# 0001 = member
if status_member_3002:
    kode_status_3002 |= 1

# 0010 = belanja >= Rp200.000
if syarat_belanja_3002:
    kode_status_3002 |= 2

# 0100 = jumlah barang >= 3
if syarat_barang_3002:
    kode_status_3002 |= 4

# 1000 = kode promo tersedia
if promo_tersedia_3002:
    kode_status_3002 |= 8

# AND (&) untuk mengecek status member
cek_member_3002 = kode_status_3002 & 1

# OR (|) untuk menggabungkan status member dan belanja
gabungan_status_3002 = 1 | 2

# XOR (^) untuk membandingkan dua kode
kode_referensi_3002 = 11
hasil_xor_3002 = kode_status_3002 ^ kode_referensi_3002

# Shift left (<<)
hasil_shift_3002 = kode_status_3002 << 1

# ==========================================
# HAK AKSES
# ==========================================

member_access_3002 = (kode_status_3002 & 1) != 0
promo_access_3002 = (kode_status_3002 & 8) != 0

free_shipping_3002 = (
    kode_promo_3002 in ["SKIRK08", "FURINA09", "COLOMBINA06"]
    and promo_tersedia_3002
)

# ==========================================
# OUTPUT DATA
# ==========================================

print("\n=== DATA PELANGGAN ===")
print("Nama Pelanggan       :", nama_3002)
print("Status Pelanggan     :", status_3002)
print("Total Belanja        : Rp", total_belanja_3002)
print("Jumlah Barang        :", jumlah_barang_3002)
print("Kode Promo           :", kode_promo_3002)

print("\n=== HASIL VALIDASI ===")
print("Belanja >= Rp200000  :", syarat_belanja_3002)
print("Jumlah Barang >= 3   :", syarat_barang_3002)
print("Status Member        :", status_member_3002)
print("Kode Promo Tersedia  :", promo_tersedia_3002)
print("Mendapatkan Diskon   :", diskon_member_3002)
print("Mendapatkan Promo    :", promo_3002)

print("\n=== HASIL PERHITUNGAN ===")
print("Besarnya Diskon      : Rp", diskon_3002)
print("Total Pembayaran     : Rp", total_pembayaran_3002)
print("Rata-rata Barang     : Rp", rata_rata_3002)
print("Sisa Jumlah Barang   :", sisa_3002)

print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses       :", kode_status_3002)
print("Member Access        :", member_access_3002)
print("Promo Access         :", promo_access_3002)
print("Free Shipping Access :", free_shipping_3002)

print("\n=== HASIL OPERATOR ===")

print("\n-- Operator Aritmatika --")
print("Total - Diskon       :", total_belanja_3002 - diskon_3002)
print("Total + Diskon       :", total_belanja_3002 + diskon_3002)
print("Total * 10%          :", total_belanja_3002 * 10 / 100)
print("Rata-rata            :", total_belanja_3002 / jumlah_barang_3002)
print("Sisa bagi            :", jumlah_barang_3002 % 2)

print("\n-- Operator Perbandingan --")
print("Belanja >= 200000    :", total_belanja_3002 >= 200000)
print("Barang >= 3          :", jumlah_barang_3002 >= 3)
print("Member == member     :", status_3002 == "member")

print("\n-- Operator Logika --")
print("Member AND Belanja   :", status_member_3002 and syarat_belanja_3002)
print("Barang OR Member     :", syarat_barang_3002 or status_member_3002)
print("NOT Member           :", not status_member_3002)

print("\n-- Operator Penugasan --")
print("Poin setelah +=      :", poin_3002)
print("Saldo setelah -=     : Rp", saldo_3002)

print("\n-- Operator Keanggotaan --")
print("Kode promo IN daftar :", kode_promo_3002 in daftar_promo_3002)
print("Kode promo NOT IN    :", kode_promo_3002 not in daftar_promo_3002)

print("\n-- Operator Identitas --")
print("Objek kode IS sama   :", identitas_sama_3002)
print("Objek kode IS NOT    :", identitas_berbeda_3002)
print("Nilai == sama        :", kode_pertama_3002 == kode_kedua_3002)

print("\n=== OPERASI BITWISE ===")
print("Kode Status Biner   :", format(kode_status_3002, "04b"))
print("Kode Status Desimal :", kode_status_3002)

print("\nAND (&)")
print("Hasil                :", format(cek_member_3002, "04b"))
print("Desimal              :", cek_member_3002)

print("\nOR (|)")
print("1 | 2                :", format(gabungan_status_3002, "04b"))
print("Desimal              :", gabungan_status_3002)

print("\nXOR (^)")
print(format(kode_status_3002, "04b"), "^",
      format(kode_referensi_3002, "04b"))
print("Hasil                :", format(hasil_xor_3002, "04b"))
print("Desimal              :", hasil_xor_3002)

print("\nSHIFT LEFT (<<)")
print(format(kode_status_3002, "04b"), "<< 1")
print("Hasil                :", format(hasil_shift_3002, "b"))
print("Desimal              :", hasil_shift_3002)

print("\n=== SELESAI ===")