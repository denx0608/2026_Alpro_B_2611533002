# Buat file dengan nama multi_if2_2611533002.py
# Buat program untuk kondisional if
# Nama variable ditambah 4 digit nim terakhir contoh: total_belanja_1234
# Program ini menggunakan fungsi input()
# Porgoram menghitung diskon belanja

# Input dari user
total_belanja_3002 = float(input("Masukan total belanja (Rp): "))

# input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_3002 = input("Apakah anda member? (y/t) :").strip().lower()
is_member_3002 = input_member_3002 in ["y", "ya"]

# input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_3002 = input("Apakah kode promo valid? (y/t): ").strip().lower()
Kode_promo_valid_3002 = input_promo_3002 in ["y", "ya"]

total_diskon_persen_3002 = 0

# Multi-if terpisah setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_3002 > 1000000:
    total_diskon_persen_3002 += 10 # Diskon belanja besar

if is_member_3002:
    total_diskon_persen_3002 += 5 # Diskon member

if Kode_promo_valid_3002:
    total_diskon_persen_3002 += 15 # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_3002 = total_belanja_3002 = (total_diskon_persen_3002 / 100)
total_bayar_3002 = total_belanja_3002 - nominal_diskon_3002

#output hasil
print("n--- rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen_3002}% (Rp {nominal_diskon_3002:,.0f})")
print(f"Total bayar  : Rp {total_bayar_3002:,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_3002}%")
# Output: Total diskon yang anda dapatkan: 30% jika belanja > 1 juta, member dan kode promo valid

