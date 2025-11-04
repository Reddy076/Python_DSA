class Solution:
    def factorial(self, N):
        """
        Recursively calculates the factorial of a number.
        
        The factorial of a non-negative integer n is the product of all positive 
        integers less than or equal to n. It is denoted by n!.
        
        For example: 5! = 5 × 4 × 3 × 2 × 1 = 120
        
        Time Complexity: O(N) - We make N recursive calls
        Space Complexity: O(N) - Due to the recursion stack
        
        Parameters:
        N (int): The number to calculate factorial for
        
        Returns:
        int: The factorial of N
        """
        # Base case: 0! = 1 and 1! = 1
        if N <= 1:
            return 1
        
        # Recursive case: N! = N × (N-1)!
        return N * self.factorial(N - 1)


if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()
    N = 5
    
    # Calculate factorial of N using recursion
    factorial_result = sol.factorial(N)
    
    # Print the result
    print(f"Factorial of {N} is: {factorial_result}")

"""
Algorithm Explanation:

This algorithm calculates the factorial of a number using recursion.

Approach:
1. Base case: If N is 0 or 1, return 1 (by definition, 0! = 1! = 1)
2. Recursive case: N! = N × (N-1)!
3. The function calls itself with N-1 until it reaches the base case

Example Walkthrough for N=5:
1. factorial(5):
   - 5 > 1, so return 5 * factorial(4)

2. factorial(4):
   - 4 > 1, so return 4 * factorial(3)

3. factorial(3):
   - 3 > 1, so return 3 * factorial(2)

4. factorial(2):
   - 2 > 1, so return 2 * factorial(1)

5. factorial(1):
   - 1 <= 1, so return 1 (base case)

Now the recursive calls return:
- factorial(1) returns 1
- factorial(2) returns 2 * 1 = 2
- factorial(3) returns 3 * 2 = 6
- factorial(4) returns 4 * 6 = 24
- factorial(5) returns 5 * 24 = 120

Output: Factorial of 5 is: 120

This demonstrates the mathematical definition of factorial:
5! = 5 × 4 × 3 × 2 × 1 = 120
"""