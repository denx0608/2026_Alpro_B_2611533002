# Buatlah file dengan nama lainnya_2611533002.py
# Nama variable ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas dalam Python

print("==================================")
print("1. OPERATOR KEANGGOTAAN")
print("==================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_3002 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_3002 = [int(angka.strip()) for angka in input_data_3002.split(",")]

nilai_dicari_3002 = int(input("Masukkan angka yang ingin dicari: "))

# Operator In
hasil_3002 = nilai_dicari_3002 in data_3002
print("\nOperator keanggotaan IN")
print(nilai_dicari_3002, "in", data_3002, "=", hasil_3002)

# Operator Not In
hasil_3002 = nilai_dicari_3002 not in data_3002
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_3002, "not in", data_3002, "=", hasil_3002)

print("\n==================================")
print("2. OPERATOR IDENTITAS")
print("==================================")

# objek1 menggunakan list dari input pengguna
objek1_3002 = data_3002

# objek2 menggunakan list dari input pengguna   
objek2_3002 = objek1_3002

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_3002 = data_3002.copy()

print("objek1_3002 =", objek1_3002)
print("objek2_3002 =", objek2_3002)
print("objek3_3002 =", objek3_3002)

# Operator Is
hasil_3002 = objek1_3002 is objek2_3002
print("\nOperator identitas IS")
print("objek1_3002 is objek2_3002 =", hasil_3002)

# Operator Is Not
hasil_3002 = objek1_3002 is not objek3_3002
print("\nOperator identitas IS NOT")
print("objek1_3002 is not objek3_3002 =", hasil_3002)

# Membandingkan identitas dan nilai
print("\nMembandingkan identitas dan nilai:")
print("objek1_3002 is objek3_3002 =", objek1_3002 is objek3_3002)
print("objek1_3002 == objek3_3002 =", objek1_3002 == objek3_3002)