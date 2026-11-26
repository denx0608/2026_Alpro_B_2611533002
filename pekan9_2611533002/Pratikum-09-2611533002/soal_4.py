kelas = input().split()
pengumpul = input().split()

set_kelas = set(kelas)
set_pengumpul = set(pengumpul)

belum = set_kelas - set_pengumpul

print(f"Submitted: {len(set_pengumpul)} students")
print(f"Not submitted: {len(belum)} students")

for nomor in kelas:
    if nomor not in set_pengumpul:
        print(nomor)