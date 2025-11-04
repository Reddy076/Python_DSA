class Solution:
    def printNum(self, num, count, N):
        """
        Recursively prints numbers from num to N.
        
        This function uses recursion to print numbers in sequence from a starting 
        number to an ending number. It uses a count parameter to track how many 
        numbers have been printed.
        
        Time Complexity: O(N) - We make N recursive calls
        Space Complexity: O(N) - Due to the recursion stack
        
        Parameters:
        num (int): The current number to print
        count (int): The count of numbers printed so far
        N (int): The total number of numbers to print
        """
        # Base case: If we've printed N numbers, stop recursion
        if count == N:
            return
        
        # Print the current number
        print(num)
        
        # Recursive call to print the next number
        self.printNum(num + 1, count + 1, N)


if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    N = 5
    
    # Print numbers from 1 to N using recursion
    solution.printNum(1, 0, N)

"""
Algorithm Explanation:

This algorithm uses recursion to print numbers from 1 to N.

Approach:
1. The function takes three parameters:
   - num: The current number to print
   - count: How many numbers have been printed so far
   - N: The total count of numbers to print
2. Base case: When count equals N, stop the recursion
3. Print the current number
4. Make a recursive call with:
   - num + 1 (next number to print)
   - count + 1 (increment the count)
   - N (unchanged)

Example Walkthrough for N=5:
1. Call printNum(1, 0, 5):
   - count(0) != N(5), so continue
   - Print 1
   - Call printNum(2, 1, 5)

2. Call printNum(2, 1, 5):
   - count(1) != N(5), so continue
   - Print 2
   - Call printNum(3, 2, 5)

3. Call printNum(3, 2, 5):
   - count(2) != N(5), so continue
   - Print 3
   - Call printNum(4, 3, 5)

4. Call printNum(4, 3, 5):
   - count(3) != N(5), so continue
   - Print 4
   - Call printNum(5, 4, 5)

5. Call printNum(5, 4, 5):
   - count(4) != N(5), so continue
   - Print 5
   - Call printNum(6, 5, 5)

6. Call printNum(6, 5, 5):
   - count(5) == N(5), so return (base case reached)

Output:
1
2
3
4
5

This demonstrates how recursion can be used to replace loops for repetitive tasks.
"""