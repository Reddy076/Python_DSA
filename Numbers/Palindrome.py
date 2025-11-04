"""
Check if a Number is a Palindrome

A palindrome number is a number that remains the same when its digits are reversed.
For example, 121, 1331, 454 are palindromes.

This program reverses the digits of a number and compares it with the original.
"""

# Number to check for palindrome
n = 454
palindrome = n
rev = 0

# Reverse the digits of the number
while (n > 0):
    c = n % 10  # Extract the last digit
    # Note: The condition "if c==0:continue" seems unnecessary and incorrect
    # It would skip zeros in the number, which is not correct for palindrome checking
    rev = rev * 10 + c  # Build the reversed number
    n //= 10  # Remove the last digit

print("Reversed number:", rev)

# Check if the reversed number equals the original number
if rev == palindrome:
    print('It is a palindrome')
else:
    print('It is not a palindrome')

"""
Algorithm Explanation:

This algorithm checks if a number is a palindrome by reversing its digits and 
comparing the reversed number with the original.

Approach:
1. Store the original number
2. Reverse the digits of the number by:
   - Extracting the last digit using modulo operator (%)
   - Building the reversed number by multiplying current result by 10 and adding the digit
   - Removing the last digit using integer division (//)
3. Compare the reversed number with the original

Example Walkthrough:
For n = 454:
1. n=454, c=4, rev=0*10+4=4, n=45
2. n=45, c=5, rev=4*10+5=45, n=4
3. n=4, c=4, rev=45*10+4=454, n=0
4. Loop ends as n=0
5. rev=454, palindrome=454
6. Since rev == palindrome, it's a palindrome

Time Complexity: O(d) where d is the number of digits
Space Complexity: O(1)

Note: The original code had an unnecessary condition "if c==0:continue" which 
would incorrectly skip zeros in the number. This has been removed for correct 
palindrome checking.
"""