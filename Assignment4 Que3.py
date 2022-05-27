"""
Assignment 4
Name: Dhruv Aggarwal
SID: 21107064
Branch: Mechanical
"""
import random

print('Assignment Question 3')

for i in range(1, 11):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    ans = int(input(f'Question {i}: {a}x{b}='))
    if ans == a * b:
        print('Right!')
    else:
        print('Wrong. The correct answer is', a * b)

