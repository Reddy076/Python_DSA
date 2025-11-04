"""
Reverse a Number

This program reverses the digits of a given number.
For example, reversing 12345 gives 54321.

The algorithm extracts each digit from the right and builds the reversed number
by multiplying the current result by 10 and adding the extracted digit.
"""

# Number to reverse
n = 125456
rev = 0

# Reverse the digits of the number
while (n > 0):
    c = n % 10  # Extract the last digit
    rev = rev * 10 + c  # Build the reversed number
    n //= 10  # Remove the last digit

# Print the reversed number
print("Reversed number:", rev)

"""
Algorithm Explanation:

This algorithm reverses a number by extracting digits from right to left and 
building the reversed number from left to right.

Approach:
1. Initialize rev = 0 to store the reversed number
2. While the original number is greater than 0:
   - Extract the last digit using modulo operator (n % 10)
   - Multiply the current reversed number by 10 and add the extracted digit
   - Remove the last digit from the original number using integer division (n //= 10)
3. The final value of rev is the reversed number

Example Walkthrough:
For n = 125456:
1. n=125456, c=6, rev=0*10+6=6, n=12545
2. n=12545, c=5, rev=6*10+5=65, n=1254
3. n=1254, c=4, rev=65*10+4=654, n=125
4. n=125, c=5, rev=654*10+5=6545, n=12
5. n=12, c=2, rev=6545*10+2=65452, n=1
6. n=1, c=1, rev=65452*10+1=654521, n=0
7. Loop ends as n=0
8. Final result: rev = 654521

Time Complexity: O(d) where d is the number of digits
Space Complexity: O(1)
"""