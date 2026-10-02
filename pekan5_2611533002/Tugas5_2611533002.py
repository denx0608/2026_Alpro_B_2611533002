print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

n_3002 = int(input("Masukkan ukuran skala jam pasir (N): "))

# =========================
# BORDER ATAS
# =========================
print("#", end="")

for i_3002 in range(4 * n_3002 + 5):
    print("=", end="")

print("#")

# =========================
# FASE 1: JAM PASIR ATAS
# =========================
for baris_3002 in range(n_3002, 0, -1):

    print("| ", end="")

    # Spasi penyeimbang kiri
    for spasi_3002 in range(2 * (n_3002 - baris_3002)):
        print(" ", end="")

    # Angka mundur
    for angka_3002 in range(baris_3002, 0, -1):
        print(angka_3002, end=" ")
    
    # Poros kristal
    print("<*>", end="")

    # Angka maju
    for angka_3002 in range(1, baris_3002 + 1):
        print(" ", end="")
        print(angka_3002, end="")

    # Spasi penyeimbang kanan
    for spasi_3002 in range(2 * (n_3002 - baris_3002)):
        print(" ", end="")

    print(" |")

# =========================
# FASE 2: POROS TENGAH
# =========================
print("|", end="")

for spasi_3002 in range(2 * n_3002 + 1):
    print(" ", end="")

print("<*>", end="")

for spasi_3002 in range(2 * n_3002 + 1):
    print(" ", end="")

print("|")

# =========================
# FASE 3: JAM PASIR BAWAH
# =========================
for baris_3002 in range(1, n_3002 + 1):

    print("| ", end="")

    # Spasi penyeimbang kiri
    for spasi_3002 in range(2 * (n_3002 - baris_3002)):
        print(" ", end="")

    # Angka mundur
    for angka_3002 in range(baris_3002, 0, -1):
        print(angka_3002, end=" ")

    # Poros kristal
    print("<*>", end="")

    # Angka maju
    for angka_3002 in range(1, baris_3002 + 1):
        print(" ", end="")
        print(angka_3002, end="")

    # Spasi penyeimbang kanan
    for spasi_3002 in range(2 * (n_3002 - baris_3002)):
        print(" ", end="")

    print(" |")

# =========================
# BORDER BAWAH
# =========================
print("#", end="")

for i_3002 in range(4 * n_3002 + 5):
    print("=", end="")

print("#")