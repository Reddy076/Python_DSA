def isSorted(arr):
    """
    Checks if an array is sorted in non-decreasing order.
    
    This function iterates through the array and compares each element with its previous element.
    If any element is smaller than its previous element, the array is not sorted.
    
    Time Complexity: O(n) - We iterate through the array once
    Space Complexity: O(1) - We only use a constant amount of extra space
    
    Parameters:
    arr (list): The input array to check
    
    Returns:
    bool: True if the array is sorted in non-decreasing order, False otherwise
    """
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # If current element is smaller than the previous element, array is not sorted
        if arr[i] < arr[i-1]:
            return False
    
    # If we reach here, all elements are in non-decreasing order
    return True


# Driver code to test the isSorted function
if __name__ == "__main__":
    # Example array
    arr = [1, 2, 3, 4, 6, 5]
    
    # Check if the array is sorted
    result = isSorted(arr)
    
    # Print the result
    if result:
        print(result, "the array is sorted")
    else:
        print(result, "the array is not sorted")

"""
Algorithm Explanation:

This algorithm checks if an array is sorted in non-decreasing order by comparing
each element with its previous element.

Approach:
1. Iterate through the array starting from the second element (index 1)
2. For each element, compare it with its previous element
3. If any element is smaller than its previous element, return False (not sorted)
4. If we complete the iteration without finding any such pair, return True (sorted)

Example Walkthrough:
For array [1, 2, 3, 4, 6, 5]:
1. i=1: arr[1]=2, arr[0]=1 => 2 >= 1, continue
2. i=2: arr[2]=3, arr[1]=2 => 3 >= 2, continue
3. i=3: arr[3]=4, arr[2]=3 => 4 >= 3, continue
4. i=4: arr[4]=6, arr[3]=4 => 6 >= 4, continue
5. i=5: arr[5]=5, arr[4]=6 => 5 < 6, return False

Final Result: False (the array is not sorted)

For a sorted array like [1, 2, 3, 4, 5, 6]:
1. i=1: arr[1]=2, arr[0]=1 => 2 >= 1, continue
2. i=2: arr[2]=3, arr[1]=2 => 3 >= 2, continue
3. i=3: arr[3]=4, arr[2]=3 => 4 >= 3, continue
4. i=4: arr[4]=5, arr[3]=4 => 5 >= 4, continue
5. i=5: arr[5]=6, arr[4]=5 => 6 >= 5, continue
6. Loop completes, return True

Final Result: True (the array is sorted)
"""