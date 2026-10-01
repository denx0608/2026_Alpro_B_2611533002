# Buat file dengan nama perulangan_for3_2611533002.py
# Buat proram untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_3002
# Program ini menggunakan fungsi input ()

ulang_3002 = int(input("Masukkan jumlah perulangan: "))

jumlah_3002 = 0
for i in range(1, ulang_3002 + 1):
    print(1, end=" ")
    jumlah_3002 += 1

    if i < ulang_3002:
        print("+", end=" ")
    else:
        print("= ", jumlah_3002, end=" ")
print()
print("jumlah =", jumlah_3002)