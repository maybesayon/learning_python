score = float(input("Enter your score "))
if score >= 1.0 or score <0.0:
    print("THe grade is invalid")
elif score >= 0.9:
    print("Your grade is A")
elif score >= 0.8:
    print("Your grade is B")
elif score >= 0.7:
    print("Your grade is C")
elif score >= 0.6:
    print("Your grade is D")
else:
    print("Your grade is F")
