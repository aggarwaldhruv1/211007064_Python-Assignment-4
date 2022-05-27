"""
Assignment 4
Name: Dhruv Aggarwal
SID: 21107064
Branch: Mechanical
"""

print("Assignment Question 1")

marks = int(input("Enter your marks to know the corresponding grade:\n"))
if marks < 25:
    print("Grade: F")
elif 25 <= marks < 45:
    print("Grade: E")
elif 45 <= marks < 50:
    print("Grade: D")
elif 50 <= marks < 60:
    print("Grade: C")
elif 60 <= marks < 80:
    print("Grade: B")
elif marks >= 80:
    print("Grade: A")
