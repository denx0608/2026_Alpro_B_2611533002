# Buat file dengan nama nested_for2_2611533002.py
# Buat proram untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_3002
# Program ini menggunakan fungsi input ()

batas_3002 = int(input("Masukkan nilai batas: "))
for i in range(1, batas_3002 + 1):
    for j in range(1, batas_3002 + 1):
        print("*", end="")
    print() # pindah ke baris berikutnya