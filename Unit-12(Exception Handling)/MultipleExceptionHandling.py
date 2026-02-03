try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))

    result = num1/num2
    print(f"Answer = {result}")

except ValueError:
    print("Please enter integer number only..")

except ZeroDivisionError:
    print("Cannot divide by zero... num2 cannot be 0")

except Exception as e:
    print("Error aayo hai")
    print(f"Your error = {e}")
