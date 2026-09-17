# Buat file dengan nama Konstanta_2611533002.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variable ditambah 4 digit nim terakhir contoh: phi_1234

from typing import Final
PI : Final = 3.14
print("pi: %f" % (PI))
jari_3002 = float(input("Masukan jari-jari lingkaran: "))
luas_3002 = PI * jari_3002 * jari_3002
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f"% (jari_3002, luas_3002))