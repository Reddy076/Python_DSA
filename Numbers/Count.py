"""
Count Digits in a Number

This program demonstrates three different approaches to count the number of digits in a number:
1. Optimal mathematical approach using logarithms
2. String conversion approach
3. Lambda function approach
"""

# Optimal Approach using logarithms
import math 

# Get the number from user
n = int(input("Enter a number to count digits: "))

# Handle special case of 0
if n == 0:
    count = 1
else:
    # For positive numbers, number of digits = floor(log10(n)) + 1
    # We use abs(n) to handle negative numbers
    count = int((math.log10(abs(n)) + 1))

print("Number of digits (using logarithm):", count)


# Brute force approach using string conversion
n = int(input("Enter a number to count digits: "))

# Convert number to string and count characters
# map(int, str(n)) converts each digit character to int, but we just need the length
count = len(str(abs(n)))
print("Number of digits (using string conversion):", count)


# Using lambda function
n = int(input("Enter a number to count digits: "))

# Sum 1 for each character in the string representation of the number
count = sum(map(lambda x: 1, str(abs(n))))
print("Number of digits (using lambda):", count)

"""
Algorithm Explanation:

This program demonstrates three different approaches to count digits in a number:

1. Mathematical Approach (Optimal):
   - Uses the mathematical property that the number of digits in a positive integer n
     is floor(log10(n)) + 1
   - For example, for 1234: log10(1234) ≈ 3.09, floor(3.09) = 3, 3 + 1 = 4 digits
   - Time Complexity: O(1)
   - Space Complexity: O(1)

2. String Conversion Approach:
   - Converts the number to a string and counts the characters
   - For example, 1234 becomes "1234" which has 4 characters
   - Time Complexity: O(d) where d is the number of digits
   - Space Complexity: O(d) for the string

3. Lambda Function Approach:
   - Uses map and lambda to count each character in the string representation
   - For example, for "1234", lambda function returns 1 for each character, sum = 4
   - Time Complexity: O(d) where d is the number of digits
   - Space Complexity: O(d) for the string

Example Walkthrough:
For number 12345:
1. Mathematical: log10(12345) ≈ 4.09, floor(4.09) + 1 = 4 + 1 = 5 digits
2. String conversion: len("12345") = 5 digits
3. Lambda: sum([1, 1, 1, 1, 1]) = 5 digits

All approaches correctly return 5 digits for the number 12345.
"""