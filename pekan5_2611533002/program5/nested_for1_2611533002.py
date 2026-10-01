# Buat file dengan nama nested_for1_2611533002.py
# Buat proram untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_3002
# Program ini menggunakan fungsi input ()

batas_3002 = int(input("Masukkan nilai batas: "))
for line_3002 in range(1, batas_3002 + 1):
    for j in range(1, (-1 * line_3002 + batas_3002) + 1):
        print(".", end="")
    print(line_3002) 