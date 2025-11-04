"""
Armstrong Number Checker

An Armstrong number (also known as a narcissistic number) is a number that is equal to 
the sum of its own digits each raised to the power of the number of digits.

For example:
- 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
- 9474 is an Armstrong number because 9^4 + 4^4 + 7^4 + 4^4 = 6561 + 256 + 2401 + 256 = 9474
"""

# Get input from user
num = int(input("Enter a number: "))
original = num
digits = len(str(num))
sum_power = 0

# Calculate sum of each digit raised to the power of number of digits
while num > 0:
    digit = num % 10  # Extract the last digit
    sum_power += digit ** digits  # Add digit raised to power of total digits
    num = num // 10  # Remove the last digit

# Check if the sum equals the original number
if sum_power == original:
    print(f"{original} is an Armstrong number!")
else:
    print(f"{original} is NOT an Armstrong number.")

"""
Algorithm Explanation:

This algorithm checks if a number is an Armstrong number by:
1. Counting the number of digits in the number
2. Extracting each digit and raising it to the power of the total number of digits
3. Summing these powered digits
4. Comparing the sum with the original number

Example Walkthrough:
For number 153:
1. digits = 3
2. Process each digit:
   - digit = 153 % 10 = 3
   - sum_power = 0 + 3^3 = 0 + 27 = 27
   - num = 153 // 10 = 15
   
   - digit = 15 % 10 = 5
   - sum_power = 27 + 5^3 = 27 + 125 = 152
   - num = 15 // 10 = 1
   
   - digit = 1 % 10 = 1
   - sum_power = 152 + 1^3 = 152 + 1 = 153
   - num = 1 // 10 = 0

3. Loop ends as num = 0
4. sum_power (153) == original (153), so it's an Armstrong number

Time Complexity: O(d) where d is the number of digits
Space Complexity: O(1)
"""