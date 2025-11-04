def removeDuplicates(arr):
    """
    Removes duplicates from a sorted array in-place and returns the new length.
    
    This function uses the two-pointer technique to remove duplicates from a sorted array.
    The first k elements of the array will contain the unique elements in their original order.
    
    Time Complexity: O(n) - We iterate through the array once
    Space Complexity: O(1) - We modify the array in-place
    
    Parameters:
    arr (list): The input sorted array (modified in-place)
    
    Returns:
    int: The number of unique elements in the array
    """
    # Handle edge case of empty array
    if not arr:
        return 0
    
    # Initialize pointer i to track the position of the last unique element
    i = 0
    
    # Iterate through the array with pointer j starting from the second element
    for j in range(1, len(arr)):
        # If current element is different from the last unique element
        if arr[i] != arr[j]:
            # Move i forward and place the new unique element at position i
            i += 1
            arr[i] = arr[j]
    
    # Return the count of unique elements (i+1 because indices are 0-based)
    return i + 1


# Driver code to test the removeDuplicates function
if __name__ == "__main__":
    # Example sorted array with duplicates
    arr = [1, 1, 2, 2, 5, 6, 6]
    
    # Remove duplicates and get the count of unique elements
    unique_count = removeDuplicates(arr)
    
    # Print the results
    print("Number of unique elements:", unique_count)
    print("Array with duplicates removed:", arr[:unique_count])

"""
Algorithm Explanation:

This algorithm removes duplicates from a sorted array using the two-pointer technique.

Approach:
1. Use two pointers: i (slow pointer) to track the position of the last unique element
   and j (fast pointer) to scan through the array
2. Initialize i to 0 (first element is always unique)
3. Iterate j from 1 to the end of the array
4. When arr[j] is different from arr[i], increment i and copy arr[j] to arr[i]
5. Return i+1 as the count of unique elements

Example Walkthrough:
For array [1, 1, 2, 2, 5, 6, 6]:
1. Initial: i=0, j=1, arr=[1, 1, 2, 2, 5, 6, 6]
2. j=1: arr[1]=1, arr[0]=1 => Equal, no change
3. j=2: arr[2]=2, arr[0]=1 => Different, i=1, arr[1]=2 => arr=[1, 2, 2, 2, 5, 6, 6]
4. j=3: arr[3]=2, arr[1]=2 => Equal, no change
5. j=4: arr[4]=5, arr[1]=2 => Different, i=2, arr[2]=5 => arr=[1, 2, 5, 2, 5, 6, 6]
6. j=5: arr[5]=6, arr[2]=5 => Different, i=3, arr[3]=6 => arr=[1, 2, 5, 6, 5, 6, 6]
7. j=6: arr[6]=6, arr[3]=6 => Equal, no change
8. Return i+1 = 4

Final Result:
- Unique count: 4
- Array with duplicates removed: [1, 2, 5, 6]
"""