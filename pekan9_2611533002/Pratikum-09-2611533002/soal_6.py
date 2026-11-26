
schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"]
}

# 6a
busiest_day = max(schedule, key=lambda day: len(schedule[day]))
count = len(schedule[busiest_day])

print(f"Busiest day: {busiest_day} ({count} courses)")

# 6b
course = input("Course: ")

total = 0
for day in schedule:
    total += schedule[day].count(course)

print(f"{course}: {total} days")
