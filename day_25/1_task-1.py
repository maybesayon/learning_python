try:
    num1 = int(input("Enter 1st number "))
    num2 = int(input("Enter 2nd number "))
    summ = num1 + num2
    print(summ)

except ValueError:
    print("Enter a NUMBER")