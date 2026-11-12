# Name: Muhammad Danish Abshori
# NIM: 2611533002
# Question 3

#soal a
text = "Informatika"
print(text[10])
text = text.upper()
print(len(text))
print(text[0:11])

#soal b
text = "Muhammad Danish Abshori"
text = text.lower()
count = 0
for char in text:
    if char in "aiueo":
        count += 1
print("Vowels:", count)
