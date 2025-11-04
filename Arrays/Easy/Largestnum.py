def findLargestElement(arr, n):
    """
    Finds the largest element in an array.
    
    This function iterates through the array and keeps track of the maximum element found so far.
    
    Time Complexity: O(n) - We iterate through the array once
    Space Complexity: O(1) - We only use a constant amount of extra space
    
    Parameters:
    arr (list): The input array of numbers
    n (int): The size of the array
    
    Returns:
    int/float: The largest element in the array
    """
    # Initialize max to negative infinity to handle negative numbers as well
    max_val = float('-inf')
    
    # Iterate through each element in the array
    for i in range(n):
        # If current element is greater than max, update max
        if arr[i] > max_val:
            max_val = arr[i]
    
    # Return the largest element found
    return max_val


# Driver code to test the findLargestElement function
if __name__ == "__main__":
    # Example array
    arr = [8, 10, 5, 7, 9]
    n = 5
    
    # Find the largest element in the array
    max_element = findLargestElement(arr, n)
    
    # Print the result
    print("The largest element in the array is:", max_element)

"""
Algorithm Explanation:

This is a simple linear search algorithm to find the maximum element in an array.

Approach:
1. Initialize a variable 'max_val' to negative infinity to handle any possible value in the array
2. Iterate through each element of the array
3. For each element, compare it with the current maximum
4. If the element is greater than the current maximum, update the maximum
5. After iterating through all elements, return the maximum value found

Example Walkthrough:
For array [8, 10, 5, 7, 9]:
1. Initialize max_val = -∞
2. Compare 8 with max_val (-∞): 8 > -∞, so max_val = 8
3. Compare 10 with max_val (8): 10 > 8, so max_val = 10
4. Compare 5 with max_val (10): 5 < 10, so max_val remains 10
5. Compare 7 with max_val (10): 7 < 10, so max_val remains 10
6. Compare 9 with max_val (10): 9 < 10, so max_val remains 10
7. Return max_val = 10

The largest element in the array is 10.
"""