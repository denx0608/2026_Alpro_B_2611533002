# Buat prograam file dengan nama aritmatika_2611533002.py
# Buat program untuk operator aritmatika dalam Python
# Buat variable ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_3002 = int(input("Masukkan angka angka-1: "))
angka2_3002 = int(input("Masukkan angka angka-2: "))

# Penjumlahan
hasil = angka1_3002 + angka2_3002
print("\nOperator penjumlahan")
print("Hasil =", hasil)    

# Pengurangan
hasil = angka1_3002 - angka2_3002
print("\nOperator Pengurangan")
print("Hasil =", hasil)

# Perkalian
hasil = angka1_3002 * angka2_3002
print("\nOperator Perkalian")
print("Hasil =", hasil)

# Pembagian
if angka2_3002 != 0:
    hasil = angka1_3002 / angka2_3002
    print("\nOperator Pembagian")
    print("Hasil =", hasil)

    hasil = angka1_3002 // angka2_3002
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil)

    hasil = angka1_3002 % angka2_3002
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil)
else:
    print("Angka kedua tidak boleh vernilai 0.")

# Pangkat
hasil = angka1_3002 ** angka2_3002
print("\nOperator Pangkat")
print("Hasil =", hasil)