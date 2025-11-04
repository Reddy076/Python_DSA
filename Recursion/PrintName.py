class Solution:
    def printName(self, name, count, N):
        """
        Recursively prints a name N times.
        
        This function uses recursion to print a given name a specified number of times.
        
        Time Complexity: O(N) - We make N recursive calls
        Space Complexity: O(N) - Due to the recursion stack
        
        Parameters:
        name (str): The name to print
        count (int): The current count of prints
        N (int): The total number of times to print the name
        """
        # Base case: If we've printed the name N times, stop recursion
        if count == N:
            return
        
        # Print the name
        print(name)
        
        # Recursive call with incremented count
        self.printName(name, count + 1, N)


if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()
    N = 5
    name = 'red'
    
    # Print the name N times using recursion
    sol.printName(name, 0, N)

"""
Algorithm Explanation:

This algorithm uses recursion to print a name a specified number of times.

Approach:
1. The function takes three parameters:
   - name: The name to print
   - count: How many times the name has been printed so far
   - N: The total number of times to print the name
2. Base case: When count equals N, stop the recursion
3. Print the name
4. Make a recursive call with incremented count

Example Walkthrough for name="red" and N=3:
1. Call printName("red", 0, 3):
   - count(0) != N(3), so continue
   - Print "red"
   - Call printName("red", 1, 3)

2. Call printName("red", 1, 3):
   - count(1) != N(3), so continue
   - Print "red"
   - Call printName("red", 2, 3)

3. Call printName("red", 2, 3):
   - count(2) != N(3), so continue
   - Print "red"
   - Call printName("red", 3, 3)

4. Call printName("red", 3, 3):
   - count(3) == N(3), so return (base case reached)

Output:
red
red
red

This demonstrates how recursion can be used to repeat actions a specific number of times.
"""