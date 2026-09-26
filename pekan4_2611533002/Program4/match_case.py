# Buat file dengan nama match_case1.py
# Buat program untuk match case
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()
# Program konversi angka menjadi nama bulan

bulan_3002 = int(input("Masukan angka bulan (1- 12): "))

match bulan_3002:
    case 1:
        print("januari")
    case 2:
        print("Februari")
    case 3:
        print("maret")
    case 4:
        print("april")
    case 5:
        print("mei")
    case 6:
        print("juni")
    case 7:
        print("juli")
    case 8:
        print("agustus")
    case 9:
        print("september")
    case 10:
        print("oktober")
    case 11:
        print("november")
    case 12:
        print("desember")
    case _:
        print("Angka tidak valid")