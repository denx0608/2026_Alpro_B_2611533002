# Buat file dengan nama Boolean_2611533002.py
# Nama variable ditambah 4 digit nim terakhir contoh: nilai_1234
# Deklarasikan variable dengan type Boolean
is_lulus_3002 = True
is_cumlaude_3002 = True

# Menggunakan Boolean
nilai_3002 = 80
batas_lulus_3002 = 75

#Menentukan nilai Boolean dari kondisi
status_kelulusan_3002 = nilai_3002 >= batas_lulus_3002 # Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai", nilai_3002)
print("Apakah Lulus?", status_kelulusan_3002)
if is_lulus_3002 and is_cumlaude_3002:
    print("Selamat, Anda lulus dengan predikat Cumlaude!")