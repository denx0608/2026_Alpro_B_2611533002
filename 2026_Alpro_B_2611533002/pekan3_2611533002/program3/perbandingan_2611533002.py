# Buatlah file dengan nama perbandingan_2611533002.py
# Nama variable ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# program operator perbandingan dalam Python

angka1_3002 = int(input("Input angka angka-1: "))    
angka2_3002 = int(input("Input angka angka-2: "))

# Lebih besar dari
hasil = angka1_3002 > angka2_3002
print("\nOperator lebih Besar dari")
print("angka1_3002 > angka2_3002 =", hasil)

# Lebih kecil dari
hasil = angka1_3002 < angka2_3002
print("\nOperator lebih Kecil dari")
print("angka1_3002 < angka2_3002 =", hasil)

# Lebih besar dari atau sama dengan
hasil = angka1_3002 >= angka2_3002
print("\nOperator lebih Besar dari atau sama dengan")
print("angka1_3002 >= angka2_3002 =", hasil)

# Lebih kecil dari atau sama dengan
hasil = angka1_3002 <= angka2_3002
print("\nOperator lebih Kecil dari atau sama dengan")
print("angka1_3002 <= angka2_3002 =", hasil)

# Sama dengan
hasil = angka1_3002 == angka2_3002
print("\nOperator sama dengan")
print("angka1_3002 == angka2_3002 =", hasil)

# Tidak sama dengan
hasil = angka1_3002 != angka2_3002
print("\nOperator tidak sama dengan")
print("angka1_3002 != angka2_3002 =", hasil)

# Tambahan: perbandingan berantai dalam Python
hasil = 0 < angka1_3002 < 100
print("\nPerbandingan berantai")
print("0 < angka1_3002 < 100 =", hasil)

hasil = 0 < angka2_3002 < 100
print("0 < angka2_3002 < 100 =", hasil)