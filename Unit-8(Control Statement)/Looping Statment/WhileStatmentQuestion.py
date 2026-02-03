#add two numbers.

while True:
    num1 = int(input("Enter first num: "))
    num2 = int(input("Enter 2nd num: "))

    result = num1+num2
    print(f"Addition = {result}")

    user_input = input("Do you want to continue again(yes/no), type y for continue or n for exit: ").lower()

    if user_input == "n":
        break  


