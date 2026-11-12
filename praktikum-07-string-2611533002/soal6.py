# Name: Muhammad Danish Abshori
# NIM: 2611533002
# Question 6


full_name = "Muhammad Danish Abshori"
nim = "2611533002"
clean = full_name.strip()
posisi_spasi = clean.find(" ")

if posisi_spasi == -1:
    nama_depan = clean
else:
    nama_depan = clean[:posisi_spasi]
username = nama_depan.lower() + nim[-3:]

print("Username:", username)
