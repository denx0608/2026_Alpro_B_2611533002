
LAST_DIGIT = 2
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []

for day in range(1, 8):
    expense = int(input(f"Day {day}: "))
    expenses.append(expense)

total = 0
highest = expenses[0]
highest_day = 1
days_above = 0

for i in range(7):
    total += expenses[i]

    if expenses[i] > highest:
        highest = expenses[i]
        highest_day = i + 1

    if expenses[i] > daily_limit:
        days_above += 1

average = total / 7

print("Daily limit:", daily_limit)
print("Total:", total)
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest})")
print("Days above limit:", days_above)
