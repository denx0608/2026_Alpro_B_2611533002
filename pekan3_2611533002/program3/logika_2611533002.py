# Buatlah file dengan nama logika_2611533002.py
# Nama variable ditambah 4 digit nim terakhir contoh: a1_1234
# Program ini menggunakan fungsi input()
# Program oprator logika dalam Python

# Memasukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1__3002 = input("Input nilai boolean-a1 (true/fa;se):").strip().lower() == "true"
a2__3002 = input("Input nilai boolean-a2 (true/false):").strip().lower() == "true"

print("\nA1 =", a1__3002)
print("A2 =", a2__3002)

# Konjungsi: bernilai True jika keduanya true
hasil = a1__3002 and a2__3002
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil)
# Disjungsi: bernilai True jika salah satunya True

hasil_3002 = a1__3002 or a2__3002
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_3002)

# Negasi A1: mambalikan nilai A1
hasil_3002 = not a1__3002
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_3002)

# Negasi A2: membalikan nilai A2
hasil_3002 = not a2__3002
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_3002)

# XOR: bernilai True jika Kedua nilai berbeda
hasil_3002 = a1__3002 != a2__3002
print("\nDisjungsi eksklusif (XOR)")
print("A1 XOR A2 =", hasil_3002)