"""
Check if a Number is Prime and Generate Prime Numbers

A prime number is a natural number greater than 1 that has no positive divisors 
other than 1 and itself. For example, 2, 3, 5, 7, 11, 13 are prime numbers.

This program checks if a given number is prime and also generates all prime 
numbers up to a given limit.
"""

# Check if a single number is prime
n = int(input("Enter a number to check if it's prime: "))

# Numbers less than 2 are not prime
if n < 2:
    print(f"{n} is NOT prime")
else:
    # Assume the number is prime until proven otherwise
    is_prime = True
    
    # Check for divisors from 2 to n-1
    for i in range(2, n):
        # If n is divisible by i, it's not prime
        if n % i == 0:
            is_prime = False
            break  # No need to check further
    
    # Print the result
    if is_prime:
        print(f"{n} is PRIME")
    else:
        print(f"{n} is NOT prime")

# Generate a list of prime numbers up to a given limit
n = int(input("Enter upper limit to find all primes up to that number: "))

print(f"Prime numbers up to {n}:")
# Check each number from 2 to n
for num in range(2, n + 1):
    # Assume the number is prime until proven otherwise
    is_prime = True
    
    # Check for divisors from 2 to num-1
    for i in range(2, num):
        # If num is divisible by i, it's not prime
        if num % i == 0:
            is_prime = False
            break  # No need to check further
    
    # If still prime, print it
    if is_prime:
        print(num, end=" ")

print()  # New line after the list of primes

"""
Algorithm Explanation:

Prime Checking Algorithm:
1. Numbers less than 2 are not prime by definition
2. For numbers >= 2, check if any number from 2 to n-1 divides it evenly
3. If a divisor is found, the number is not prime
4. If no divisors are found, the number is prime

Prime Generation Algorithm:
1. For each number from 2 to the given limit:
   - Check if it's prime using the same method as above
   - If prime, print it

Example Walkthrough:

Checking if 17 is prime:
1. 17 >= 2, so continue
2. Check divisors from 2 to 16:
   - 17 % 2 = 1, not divisible
   - 17 % 3 = 2, not divisible
   - 17 % 4 = 1, not divisible
   - ...continuing this process
   - No divisors found
3. 17 is PRIME

Checking if 15 is prime:
1. 15 >= 2, so continue
2. Check divisors:
   - 15 % 2 = 1, not divisible
   - 15 % 3 = 0, divisible!
3. 15 is NOT prime

Time Complexity:
- Single prime check: O(n)
- Prime generation: O(n^2)

Space Complexity: O(1)

Note: This is a basic approach. More efficient algorithms like the Sieve of 
Eratosthenes can generate all primes up to n in O(n log log n) time.
"""