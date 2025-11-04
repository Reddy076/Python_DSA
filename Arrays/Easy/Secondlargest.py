def findLargestElement(arr, n):
    """
    Finds both the second largest and second smallest elements in an array.
    
    This function iterates through the array twice to find the second largest and second smallest elements.
    In the first pass, it finds the second largest element.
    In the second pass, it finds the second smallest element.
    
    Time Complexity: O(n) - We iterate through the array twice (2*n operations)
    Space Complexity: O(1) - We only use a constant amount of extra space
    
    Parameters:
    arr (list): The input array of numbers
    n (int): The size of the array
    
    Returns:
    tuple: A tuple containing (second_largest, second_smallest)
    """
    # Initialize variables to track largest and second largest
    max_val = second_max = float('-inf')
    # Initialize variables to track smallest and second smallest
    min_val = second_min = float('inf')
    
    # First pass: Find the second largest element
    for i in range(n):
        # If current element is greater than max, update both max and second_max
        if arr[i] > max_val:
            second_max = max_val
            max_val = arr[i]
        # If current element is greater than second_max but not equal to max, update second_max
        elif arr[i] > second_max and arr[i] != max_val:
            second_max = arr[i]
    
    # Second pass: Find the second smallest element
    for i in range(n):
        # If current element is smaller than min, update both min and second_min
        if arr[i] < min_val:
            second_min = min_val
            min_val = arr[i]
        # If current element is smaller than second_min but not equal to min, update second_min
        elif arr[i] < second_min and arr[i] != min_val:
            second_min = arr[i]
    
    # Return both second largest and second smallest elements
    return second_max, second_min


# Driver code to test the findLargestElement function
if __name__ == "__main__":
    # Example array
    arr = [8, 10, 5, 7, 9]
    n = 5
    
    # Find the second largest and second smallest elements
    second_largest, second_smallest = findLargestElement(arr, n)
    
    # Print the results
    print("The second largest element in the array is:", second_largest)
    print("The second smallest element in the array is:", second_smallest)

"""
Algorithm Explanation:

This algorithm finds both the second largest and second smallest elements in an array
using two separate passes through the array.

Approach:
1. Initialize four variables:
   - max_val and second_max to negative infinity
   - min_val and second_min to positive infinity
2. First Pass (Finding Second Largest):
   - For each element, if it's greater than max_val, update both second_max and max_val
   - Else if it's greater than second_max but not equal to max_val, update second_max
3. Second Pass (Finding Second Smallest):
   - For each element, if it's smaller than min_val, update both second_min and min_val
   - Else if it's smaller than second_min but not equal to min_val, update second_min
4. Return both second_largest and second_smallest

Example Walkthrough:
For array [8, 10, 5, 7, 9]:
First Pass (Finding Second Largest):
1. Element 8: max_val = 8, second_max = -∞
2. Element 10: 10 > 8, so second_max = 8, max_val = 10
3. Element 5: 5 < 10, and 5 < 8, so no change
4. Element 7: 7 < 10, and 7 < 8, so no change
5. Element 9: 9 < 10, but 9 > 8, so second_max = 9
Result: second_largest = 9

Second Pass (Finding Second Smallest):
1. Element 8: min_val = 8, second_min = ∞
2. Element 10: 10 > 8, so no change
3. Element 5: 5 < 8, so second_min = 8, min_val = 5
4. Element 7: 7 > 5, but 7 < 8, so second_min = 7
5. Element 9: 9 > 5, and 9 > 7, so no change
Result: second_smallest = 7

Final Results:
- Second Largest Element: 9
- Second Smallest Element: 7
"""