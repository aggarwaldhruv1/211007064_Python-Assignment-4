"""
Assignment 4
Name: Dhruv Aggarwal
SID: 21107064
Branch: Mechanical
"""

year = int(input("Enter the year you want to check: "))
divisible_by_400 = year % 400

divisible_by_100 = year % 100

divisible_by_4 = year % 4

if divisible_by_400 == 0:
    print("Leap year")

elif divisible_by_100 == 0:
    print("Not a leap year")

elif divisible_by_4 == 0:
    print("Leap year")

else:
    print("Not a leap year")
