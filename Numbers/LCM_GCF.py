"""
Find LCM (Least Common Multiple) and GCF (Greatest Common Factor) of Two Numbers

This program calculates the LCM and GCF of two numbers using different algorithms.
- LCM is the smallest positive integer that is divisible by both numbers
- GCF (also known as GCD - Greatest Common Divisor) is the largest positive integer 
  that divides both numbers without remainder
"""

# LCM (Least Common Multiple)
n1 = 12
n2 = 18

# Start checking from the larger number
start = max(n1, n2)

# Find the first number that is divisible by both n1 and n2
for i in range(start, n1 * n2 + 1):
    if (i % n1 == 0 and i % n2 == 0):
        print("LCM of", n1, "and", n2, "is:", i)
        break

# GCF (Greatest Common Factor) using Euclidean Algorithm
n1 = 12
n2 = 18

# Apply Euclidean algorithm: GCF(a,b) = GCF(b, a%b) until b becomes 0
while n2 != 0:
    n1, n2 = n2, n1 % n2

print("GCF of 12 and 18 is:", n1)

"""
Algorithm Explanation:

1. LCM Calculation:
   - Start from the larger of the two numbers
   - Check each number sequentially until we find one divisible by both input numbers
   - That number is the LCM

2. GCF Calculation using Euclidean Algorithm:
   - Based on the principle: GCF(a,b) = GCF(b, a%b)
   - Continue until one number becomes 0
   - The other number is the GCF

Example Walkthrough:

For LCM of 12 and 18:
- start = max(12, 18) = 18
- Check 18: 18%12 = 6 ≠ 0, so not divisible by 12
- Check 19: 19%12 ≠ 0, 19%18 ≠ 0
- ...continue checking
- Check 36: 36%12 = 0 and 36%18 = 0, so LCM = 36

For GCF of 12 and 18 using Euclidean Algorithm:
1. n1=12, n2=18
2. n1=18, n2=12%18=12
3. n1=12, n2=18%12=6
4. n1=6, n2=12%6=0
5. n2=0, so GCF = 6

Time Complexity:
- LCM: O(LCM) in worst case
- GCF: O(log(min(a,b)))

Space Complexity: O(1) for both algorithms

Note: There's a mathematical relationship: LCM(a,b) * GCF(a,b) = a * b
So LCM can also be calculated as (a * b) / GCF(a, b) which is more efficient.
"""