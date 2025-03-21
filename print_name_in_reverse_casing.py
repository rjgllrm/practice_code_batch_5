fullname = input("Enter your full name: ")
result = ""

for char in fullname:
    if char.islower():
        result += char.upper()
    else:
        result += char.lower()

print(result)
