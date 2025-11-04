"""
Find All Divisors of a Number

This program finds and prints all divisors of a given number.
A divisor of a number n is an integer that divides n evenly (with no remainder).

For example, divisors of 36 are: 1, 2, 3, 4, 6, 9, 12, 18, 36
"""

# Number to find divisors for
n = 36

# Find and print all divisors
for i in range(1, n + 1):
    # If i divides n evenly (remainder is 0), then i is a divisor
    if (n % i == 0):
        print(i)

"""
Algorithm Explanation:

This algorithm finds all divisors of a number by checking each integer from 1 to n.

Approach:
1. Iterate through all numbers from 1 to n
2. For each number i, check if n is divisible by i (n % i == 0)
3. If divisible, i is a divisor of n, so print it

Example Walkthrough:
For n = 36:
1. i=1: 36 % 1 = 0, so 1 is a divisor
2. i=2: 36 % 2 = 0, so 2 is a divisor
3. i=3: 36 % 3 = 0, so 3 is a divisor
4. i=4: 36 % 4 = 0, so 4 is a divisor
5. i=5: 36 % 5 = 1, so 5 is not a divisor
6. i=6: 36 % 6 = 0, so 6 is a divisor
7. i=7: 36 % 7 = 1, so 7 is not a divisor
8. i=8: 36 % 8 = 4, so 8 is not a divisor
9. i=9: 36 % 9 = 0, so 9 is a divisor
10. i=10: 36 % 10 = 6, so 10 is not a divisor
...continuing this process up to i=36

Final Output:
1
2
3
4
6
9
12
18
36

Time Complexity: O(n)
Space Complexity: O(1)

Note: A more efficient approach would only check up to √n and print both i and n/i
when i is a divisor, which would reduce time complexity to O(√n).
"""