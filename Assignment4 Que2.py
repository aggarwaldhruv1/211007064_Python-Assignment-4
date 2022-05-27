"""
Assignment 4
Name: Dhruv Aggarwal
SID: 21107064
Branch: Mechanical
"""

print('Assignment Question 2')
year = int(input("Enter an year to know if its a leap year or not:\n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Not a leap year")
else:
    print("Not a leap year")