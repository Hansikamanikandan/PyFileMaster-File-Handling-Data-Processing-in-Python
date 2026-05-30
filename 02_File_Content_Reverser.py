source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

with open(source, "r") as file:
    data = file.read()

reversed_data = data[::-1]

with open(destination, "w") as file:
    file.write(reversed_data)

print("File reversed successfully")
