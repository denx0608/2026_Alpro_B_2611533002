tinggi_3002 = int(input("Masukkan tinggi segitiga: "))

for i_3002 in range(1, tinggi_3002 + 1):
    print(" " * (tinggi_3002 - i_3002), end=" ")

    for j_3002 in range(i_3002):
        print("*", end=" ")

    print()