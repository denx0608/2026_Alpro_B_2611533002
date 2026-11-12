#bonus

kalimat = input("Masukkan kalimat: ")

# Mengubah huruf menjadi kecil dan menghapus spasi
clean = kalimat.lower().replace(" ", "")

# Memeriksa palindrome
if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
