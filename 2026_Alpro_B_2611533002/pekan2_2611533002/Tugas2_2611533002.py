from typing import Final

BATAS_LULUS: Final = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_3002 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_3002 = input("Masukkan Jenis Kelamin (L/P): ")
umur_3002 = int(input("Masukkan Umur : "))
skor_3002 = float(input("Masukkan Skor Tes Awal : "))

alamat_3002 = """
    Desa Simpang Empat
    Kec. Danau Kerinci
    Kab. Kerinci
"""

id_token_3002 = 100 + 3j

lulus_3002 = skor_3002 >= BATAS_LULUS

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print(f"Nama Mahasiswa : {nama_3002} | Tipe: {type(nama_3002)}")
print(f"Jenis Kelamin : {jenis_kelamin_3002} | Tipe: {type(jenis_kelamin_3002)}")
print(f"Alamat Domisili:\n{alamat_3002} | Tipe: {type(alamat_3002)}")
print(f"Umur : {umur_3002} tahun | Tipe: {type(umur_3002)}")
print(f"Skor Tes Awal : {skor_3002} | Tipe: {type(skor_3002)}")
print(f"ID Token Sinyal: {id_token_3002} | Tipe: {type(id_token_3002)}")

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print(f"Batas Minimum Nilai: {BATAS_LULUS}")
print(f"Apakah Dinyatakan Lulus?: {lulus_3002} | Tipe: {type(lulus_3002)}") 