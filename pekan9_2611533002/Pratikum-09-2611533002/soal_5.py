
n = int(input())

cash = {}

for i in range(n):
    data = input().split()
    nama = data[0]
    nominal = int(data[1])

    if nama in cash:
        cash[nama] += nominal
    else:
        cash[nama] = nominal

total = sum(cash.values())

for nama, nominal in cash.items():
    print(f"{nama}: {nominal}")

top_nama = max(cash, key=cash.get)

print(f"Total cash: {total}")
print(f"Top contributor: {top_nama} ({cash[top_nama]})")