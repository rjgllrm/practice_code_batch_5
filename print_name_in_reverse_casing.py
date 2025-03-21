fullname = input("Enter your full name: ")
result = "".join(char.upper() if char.islower() else char.lower() for char in fullname)
print(result)
