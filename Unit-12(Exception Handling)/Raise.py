age = int(input("Enter your age: "))

if age<0:
    raise ValueError("Age cannot be less than 0")

print(f"you age is {age}")