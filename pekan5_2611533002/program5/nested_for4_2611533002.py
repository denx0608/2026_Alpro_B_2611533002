# Buat file dengan nama nested_for4_2611533002.py
# Buat proram untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_3002
# Program ini menggunakan fungsi input ()

tinggi_3002 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3002 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_3002 = tinggi_3002
    c_3002 = a_3002
    lebar_3002 = (2 * tinggi_3002) - 2

    for i_3002 in range(1, tinggi_3002 + 1):
        b_3002 = c_3002 + 1

        for j_3002 in range(1, lebar_3002 + 1):

            #Baris atas dan bawah
            if i_3002 == 1 or i_3002 == tinggi_3002:
                 if j_3002 == 1 or j_3002 == lebar_3002:
                    print("#", end="")
                 else:
                    print("=", end="")
            #Baris isi
            else:
                if j_3002 == 1 or j_3002 == lebar_3002:
                    print("|", end="")
                else:
                    if j_3002 == c_3002:
                        print("<", end="")
                    elif j_3002 == b_3002:
                        print(">", end="")
                    elif j_3002 == (lebar_3002 - c_3002):
                        print("<", end="")
                    elif j_3002 == (lebar_3002 - c_3002 + 1):
                        print(">", end="")
                    elif j_3002 > b_3002 and j_3002 < (lebar_3002 - c_3002):
                        print(".", end="")
                    else:
                        print(" ", end="")
        print()

        # Logika asli Java
        a_3002 -= 2

        if a_3002 <= 0:
            c_3002 = (-a_3002) + 2
        else:
            c_3002 = a_3002