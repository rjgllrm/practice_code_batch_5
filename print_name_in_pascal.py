fullname = input("Enter your full name: ")
result = ""  # Initialize an empty string

for word in fullname.split():
    result += word.capitalize()  # Capitalize each word and add to result

print(result)
