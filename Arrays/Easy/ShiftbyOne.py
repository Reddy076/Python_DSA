def shiftByOne(arr):

    # #  left shift
    # if not arr:
    #     return 0
    # n=len(arr)
    # temp = arr[:d] 
    # for i in range(d, n):
    #     arr[i - d] = arr[i]
    # for i in range(d):
    #     arr[n - d + i] = temp[i]
    
    # return arr 
    """
    Shifts all elements in the array by one position to the left.
    
    This function moves each element one position to the left, with the first element
    moving to the end of the array. For example, [1,2,3,4,5] becomes [2,3,4,5,1].
    
    Time Complexity: O(n) - We iterate through the array once
    Space Complexity: O(1) - We only use a constant amount of extra space
    
    Parameters:
    arr (list): The input array to be shifted
    
    Returns:
    list: The shifted array
    """
    # Handle edge case of empty array
    if not arr:
        return []
    
    # Shift each element one position to the left
    for j in range(0, len(arr)-1):
        arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr


# Driver code to test the shiftByOne function
if __name__ == "__main__":
    # Example array
    arr = [1, 2, 3, 4, 5, 6, 7]
    
    # Perform left shift by one position
    shifted_array = shiftByOne(arr)
    
    # Print the result
    print("Array after left shift by one position:", shifted_array)

"""
Algorithm Explanation:

This algorithm shifts all elements in the array by one position to the left,
with the first element moving to the end of the array.

Approach:
1. Iterate through the array from the first element to the second-to-last element
2. Swap each element with its next element
3. This effectively moves all elements one position to the left

Example Walkthrough:
For array [1, 2, 3, 4, 5, 6, 7]:
1. j=0: Swap arr[0] and arr[1] => [2, 1, 3, 4, 5, 6, 7]
2. j=1: Swap arr[1] and arr[2] => [2, 3, 1, 4, 5, 6, 7]
3. j=2: Swap arr[2] and arr[3] => [2, 3, 4, 1, 5, 6, 7]
4. j=3: Swap arr[3] and arr[4] => [2, 3, 4, 5, 1, 6, 7]
5. j=4: Swap arr[4] and arr[5] => [2, 3, 4, 5, 6, 1, 7]
6. j=5: Swap arr[5] and arr[6] => [2, 3, 4, 5, 6, 7, 1]

Final Result: [2, 3, 4, 5, 6, 7, 1]

Note: This is actually a left shift by one position, not a removal of duplicates
as suggested by the original function name.
"""

 