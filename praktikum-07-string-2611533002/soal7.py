# Name: Muhammad Danish Abshori
# NIM: 2611533002
# Question 7


name = "Muhammad Danish Abshori"
nim = "2611533002"

username = name[:name.find(" ")].lower() + nim[-3:]
intake = "20" + nim[:2]
print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print("=" * 30)
