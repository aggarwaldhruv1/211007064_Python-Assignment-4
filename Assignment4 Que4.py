"""
Assignment 4
Name: Dhruv Aggarwal
SID: 21107064
Branch: Mechanical
"""
"""
We know pieces of candy in jar are less than 200, so we can assign a range of 200 to our variable.
Then, we apply 'if' statement to get the output.
Since remainders on division by 5, 6, & 7 are given,
we use '%' operator with 'and' to fulfil all 3 conditions and get the required answer
"""

print('Assignment Question 4')
for candy_in_jar in range(200):
    if candy_in_jar % 5 == 2 and candy_in_jar % 6 == 3 and candy_in_jar % 7 == 2:
        print("Number of candy pieces in the bowl are",candy_in_jar)
