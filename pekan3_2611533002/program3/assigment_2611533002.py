# bualah file dengan nama assigment_2611533002.py
# Nama variable ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assigment dalam Python

angka1_3002 = int(input("Input angka angka-1: "))
angka2_3002 = int(input("Input angka angka-2: "))

print("nNilai awal angka1 =", angka1_3002)
print("Nilai awal angka2 =", angka2_3002)

# Assigment biasa
hasil_3002 = angka1_3002
hasil_3002 += angka2_3002
print("\nAssignment penambahan (+=)")
print("hasil =", hasil_3002)

# Assignment penambahan
hasil = angka1_3002
hasil += angka2_3002
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil)

# Assignment pengurangan
hasil_3002 = angka1_3002
hasil_3002 -= angka2_3002
print("\nAssignment pengurangan (-=)")
print("hasil =", hasil_3002)

# Assignment perkalian
hasil_3002 = angka1_3002
hasil_3002 *= angka2_3002
print("\nAssignment perkalian (*=)")
print("hasil =", hasil_3002)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3002 != 0:
    hasil_3002 = angka1_3002
    hasil_3002 /= angka2_3002
    print("\nAssignment pembagian (/=)")
    print("hasil =", hasil_3002)

    #Operator tambahan
    hasil_3002 = angka1_3002
    hasil_3002 //= angka2_3002
    print("\nAssignment pembagian bulat (//=)")
    print("hasil =", hasil_3002)
    hasil_3002 = angka1_3002
    hasil_3002 %= angka2_3002
    print("\nAssignment sisa bagi (%=)")
    print("hasil =", hasil_3002)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil_3002 = angka1_3002
hasil_3002 **= angka2_3002
print("\nAssignment perpangkatan (**=)")
print("hasil =", hasil_3002)