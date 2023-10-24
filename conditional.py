age = 25
if age < 20:
    print('Eligible to drive')
else:
    print('Not eligible to drive')

# if_elif_else
marks = int(input("What did you score?\n"))
if marks > 70:
    print("Grade A")
elif marks > 60 and marks <= 70:
    print("Grade B")
elif marks > 50 and marks <= 60:
    print("Grade C")
elif marks > 40 and marks <= 50:
    print("Grade D")
else:
    print("You failed")
