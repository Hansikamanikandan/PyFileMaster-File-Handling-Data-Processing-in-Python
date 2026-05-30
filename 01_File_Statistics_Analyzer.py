filename = input("Enter file name: ")

with open(filename, "r") as file:
    data = file.read()

characters = len(data)
words = len(data.split())
vowels = sum(1 for ch in data.lower() if ch in "aeiou")

with open(filename, "r") as file:
    lines = len(file.readlines())

print("Characters:", characters)
print("Words:", words)
print("Vowels:", vowels)
print("Lines:", lines)
