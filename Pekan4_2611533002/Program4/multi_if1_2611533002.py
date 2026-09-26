# Buat file dengan nama multi_if1_2611533002.py
# Buat program untuk kondisional if
# Nama variable ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_3002 = int(input("Input Umur Anda = "))
sim_3002 = input("Apakah Anda Sudah Punya Sim C (y/t)")[0]

if umur_3002 >= 17 and sim_3002 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")

if umur_3002 >= 17 and sim_3002 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

if umur_3002 < 17 and sim_3002 == 'y':
    print("Anda Belum Cukup Umur Punya SIM")

if umur_3002 < 17 and sim_3002 != 'y':
    print("Anda Belum Cukup Umur bawa motor")
