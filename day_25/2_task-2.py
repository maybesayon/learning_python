try:
    num1 = int(input("Enter first number "))
    num2 = int(input("Enter second number "))
    result = num1 / num2
    print(result)
except ValueError:
    print("Enter a NUMBER")
except ZeroDivisionError:
    print("Enter a number greater than 0")
