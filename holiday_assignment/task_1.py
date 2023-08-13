hours = int(input("Enter the number of hours worked "))
pay = float(input("Enter the hourly pay "))
if hours <= 40:
    print(f"The pay is {pay*hours}")
elif hours > 40:
    extra_hours = (hours - 40)
    print(f"The pay is {(pay*40 + ((1.5*pay)*extra_hours))}")

