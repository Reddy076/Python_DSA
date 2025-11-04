class Solution:
    def sumOfNumbers(self, N):
        """
        Recursively calculates the sum of first N natural numbers.
        
        This function uses recursion to calculate the sum: 1 + 2 + 3 + ... + N
        
        Time Complexity: O(N) - We make N recursive calls
        Space Complexity: O(N) - Due to the recursion stack
        
        Parameters:
        N (int): The number up to which to calculate the sum
        
        Returns:
        int: The sum of first N natural numbers
        """
        # Base case: If N is 0 or 1, return N
        if N <= 1:
            return N
        
        # Recursive case: N + sum of (N-1) numbers
        return N + self.sumOfNumbers(N - 1)


if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()
    N = 5
    
    # Calculate sum of first N natural numbers using recursion
    sum_result = sol.sumOfNumbers(N)
    
    # Print the result
    print(f"Sum of first {N} natural numbers is: {sum_result}")

"""
Algorithm Explanation:

This algorithm calculates the sum of first N natural numbers using recursion.

Approach:
1. Base case: If N is 0 or 1, return N
2. Recursive case: Return N + sum of first (N-1) natural numbers
3. The function calls itself with N-1 until it reaches the base case

Example Walkthrough for N=5:
1. sumOfNumbers(5):
   - 5 > 1, so return 5 + sumOfNumbers(4)

2. sumOfNumbers(4):
   - 4 > 1, so return 4 + sumOfNumbers(3)

3. sumOfNumbers(3):
   - 3 > 1, so return 3 + sumOfNumbers(2)

4. sumOfNumbers(2):
   - 2 > 1, so return 2 + sumOfNumbers(1)

5. sumOfNumbers(1):
   - 1 <= 1, so return 1 (base case)

Now the recursive calls return:
- sumOfNumbers(1) returns 1
- sumOfNumbers(2) returns 2 + 1 = 3
- sumOfNumbers(3) returns 3 + 3 = 6
- sumOfNumbers(4) returns 4 + 6 = 10
- sumOfNumbers(5) returns 5 + 10 = 15

Output: Sum of first 5 natural numbers is: 15

This demonstrates the mathematical formula:
Sum = 1 + 2 + 3 + 4 + 5 = 15

Note: This can also be calculated using the formula N*(N+1)/2
"""