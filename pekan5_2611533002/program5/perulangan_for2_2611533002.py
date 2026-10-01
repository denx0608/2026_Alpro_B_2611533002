# Buat file dengan nama perulangan_for2_2611533002.py
# Buat proram untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_3002
# Program ini menggunakan fungsi input ()

ulang_3002 = int(input("Masukkan jumlah perulangan: "))
print("Perulangan ke-0 sampai ke-", ulang_3002)
for i in range(ulang_3002):
    print(1, end=" " )
print()
print("Perulangan ke-1 sampai ke-", ulang_3002)
for i in range(1, ulang_3002+1):
    print(i, end=" ")