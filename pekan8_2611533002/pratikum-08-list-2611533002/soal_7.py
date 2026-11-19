
menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
sales = []

for day in range(3):
    row = []
    for menu in menus:
        row.append(int(input(f"Day {day+1}, {menu}: ")))
    sales.append(row)

print("Total per day:")
for i in range(3):
    total = 0
    for x in sales[i]:
        total += x
    print(f"Day {i+1}: {total}")

menu_totals = []
for j in range(3):
    total = 0
    for i in range(3):
        total += sales[i][j]
    menu_totals.append((menus[j], total))

print("Total per menu:", menu_totals)

best_name, best_total = menu_totals[0]
for name, total in menu_totals:
    if total > best_total:
        best_name, best_total = name, total

print(f"Best seller: {best_name} ({best_total})")
