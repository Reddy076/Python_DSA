"""
Pattern Printing Programs

This file contains solutions to common pattern printing problems.
Patterns are often used to understand loops and control structures.
"""

# Problem 1: Print a square of stars
print("Problem 1: Square Pattern")
n = 5

for i in range(n):
    print('* ' * n)

print("\n" + "="*30 + "\n")

# Problem 2: Print a right-angled triangle of stars
print("Problem 2: Right Triangle Pattern")
n = 4

for i in range(n):
    print('* ' * (i + 1))

"""
Pattern Printing Explanation:

Problem 1: Square Pattern
- Prints n rows, each with n stars
- For n=5:
  * * * * *
  * * * * *
  * * * * *
  * * * * *
  * * * * *

Problem 2: Right Triangle Pattern
- Prints n rows, with the ith row containing i stars
- For n=4:
  *
  * *
  * * *
  * * * *

These patterns help in understanding:
1. Nested loops
2. String repetition in Python
3. How loop variables change
4. Basic control structures

Time Complexity: O(n^2) for both patterns
Space Complexity: O(1) - Only using a constant amount of extra space
"""

# Additional common patterns that can be added:

# Problem 3: Inverted Right Triangle
# n = 5
# for i in range(n, 0, -1):
#     print('* ' * i)

# Problem 4: Number Triangle
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()