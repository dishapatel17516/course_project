
name = input("Enter candidate name: ")
age = input("Enter age: ")
gender = input("Enter gender: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")
address = input("Enter address: ")
city = input("Enter city: ")
qualification = input("Enter highest qualification: ")
experience = input("Enter years of experience: ")
position = input("Enter position applied for: ")

print("\n--- Candidate Details ---")

print("Name          :", name)
print("Age           :", age)
print("Gender        :", gender)
print("Phone         :", phone)
print("Email         :", email)
print("Address       :", address)
print("City          :", city)
print("Qualification :", qualification)
print("Experience    :", experience)
print("Position      :", position)

# Save to a file
with open("candidates.txt", "a") as f:
    f.write(f"{name}, {age}, {gender}, {phone}, {email}, "
            f"{address}, {city}, {qualification}, "
            f"{experience}, {position}\n")
print("\nCandidate registered successfully!")
