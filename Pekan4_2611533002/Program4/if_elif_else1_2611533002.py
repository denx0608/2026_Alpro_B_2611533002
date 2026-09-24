# Buat file dengan nama if_elif_else1_2611533002.py
# Buat program untuk kondisional if
# Nama variable ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_3002 = int(input("Input Umur anda:"))
sim_3002 = input("Apakah sudah dewasa dan boleh bawa motor")

if umur_3002 >= 17 and sim_3002 == 'y':
    print("Apakah anda sudah punya SIM C: ")[0]
elif umur_3002 >= 17 and sim_3002 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")
elif umur_3002 <= 17 and sim_3002 == 'y':
    print("Anda belum cukup umur punya SIM")
else:
    print("Anda belum cukup umur dan tidak boleh bawa motor")
print("program Selesa")