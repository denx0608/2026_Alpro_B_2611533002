# Buat file dengan nama jumlah_genap_2611533002.py
# Buat program unutk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_3002
# Program ini menggunakan fungsi input ()

ulang_3002 = int(input("Masukkan nilai batas: "))

jumlah_3002 = 0
for i in range(1, ulang_3002 + 1):
    if i % 2 == 0:
        print(i, end=" ")
        jumlah_3002 = jumlah_3002 + i

        if i < ulang_3002:
            print(" + ", end="")
        else:
            print(" = ", jumlah_3002, end=" ")
print()
print("jumlah =", jumlah_3002)