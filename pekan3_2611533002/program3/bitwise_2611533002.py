# Buatlah file dengan nama bitwise_2611533002.py
# Nama variable ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator bitwise dalam Python

print("\n==================================")
print("3. OPERATOR BITWISE")
print("==================================")

angka1_3002 = int(input("Masukkan angka bitwise-1: "))
angka2_3002 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner:")
print("Angka 1:", angka1_3002, "-| biner", bin(angka1_3002))
print("Angka 2:", angka2_3002, "-| biner", bin(angka2_3002))

# Bitwise AND
hasil_3002 = angka1_3002 & angka2_3002
print("\nBitwise AND (&)")
print(angka1_3002, "&", angka2_3002, "=", hasil_3002)
print("Biner hasil =", bin(hasil_3002))
print("Biner hasil (8 bit) =", format(hasil_3002, '08b'))

# Bitwise OR
hasil_3002 = angka1_3002 | angka2_3002
print("\nBitwise OR (|)")
print(angka1_3002, "|", angka2_3002, "=", hasil_3002)
print("Biner hasil =", bin(hasil_3002))
print("Biner hasil (8 bit) =", format(hasil_3002, '08b'))

# Bitwise XOR
hasil_3002 = angka1_3002 ^ angka2_3002
print("\nBitwise XOR (^)")
print(angka1_3002, "^", angka2_3002, "=", hasil_3002)
print("Biner hasil =", bin(hasil_3002))
print("Biner hasil (8 bit) =", format(hasil_3002, '08b'))

# Bitwise NOT
hasil_3002 = ~angka1_3002
print("\nBitwise NOT (~)")
print("~", angka1_3002, "=", hasil_3002)
print("Biner hasil =", bin(hasil_3002))
print("Biner hasil (8 bit) =", format(hasil_3002, '08b'))

# Bitwise geser kiri
jumlah_geser_3002 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_3002 = angka1_3002 << jumlah_geser_3002
print("\nBitwise Geser Kiri (<<)")
print(angka1_3002, "<<", jumlah_geser_3002, "=", hasil_3002)
print("Biner hasil =", bin(hasil_3002))
print("Biner hasil (8 bit) =", format(hasil_3002, '08b'))

# Bitwise geser kanan
hasil_3002 = angka1_3002 >> jumlah_geser_3002
print("\nBitwise Geser Kanan (>>)")
print(angka1_3002, ">>", jumlah_geser_3002, "=", hasil_3002)
print("Biner hasil =", bin(hasil_3002))
print("Biner hasil (8 bit) =", format(hasil_3002, '08b'))