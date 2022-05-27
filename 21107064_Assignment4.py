"""
Assignment 4
Name: Dhruv Aggarwal
SID: 21107064
Branch: Mechanical
"""
import random

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


print('Assignment Question 3')

for i in range(1, 11):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    ans = int(input(f'Question {i}: {a}x{b}='))
    if ans == a * b:
        print('Right!')
    else:
        print('Wrong. The correct answer is', a * b)


print('Assignment Question 4')
for i in range(200):
    if i % 5 == 2 and i % 6 == 3 and i % 7 == 2:
        print("Answer:", i)
