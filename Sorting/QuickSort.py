def quickSort(arr, start, end):
    """
    Recursively sorts an array using the QuickSort algorithm.
    
    QuickSort is a divide-and-conquer algorithm that works by selecting a 'pivot' element
    from the array and partitioning the other elements into two sub-arrays, according to
    whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.
    
    Time Complexity: 
    - Best/Average Case: O(n log n)
    - Worst Case: O(n^2) - when the pivot is always the smallest or largest element
    
    Space Complexity: O(log n) - due to recursive calls
    
    Parameters:
    arr (list): The array to be sorted
    start (int): Starting index of the array segment
    end (int): Ending index of the array segment
    """
    # Base case: If the segment has one or no elements, it's already sorted
    if start >= end:
        return
    
    # Partition the array and get the pivot index
    partition_index = func(arr, start, end)
    
    # Recursively sort elements before the pivot
    quickSort(arr, start, partition_index - 1)
    
    # Recursively sort elements after the pivot
    quickSort(arr, partition_index + 1, end)


def func(arr, start, end):
    """
    Partitions the array around a pivot element.
    
    This function selects the first element as the pivot and rearranges the array
    so that all elements smaller than the pivot come before it, and all elements
    greater than the pivot come after it.
    
    Parameters:
    arr (list): The array to be partitioned
    start (int): Starting index of the array segment
    end (int): Ending index of the array segment
    
    Returns:
    int: The final position of the pivot element
    """
    # Select the first element as the pivot
    pivot = arr[start]
    
    # Initialize two pointers
    i = start  # Points to the first element
    j = end    # Points to the last element
    
    # Continue until the pointers cross each other
    while i < j:
        # Move i to the right while elements are less than or equal to pivot
        while arr[i] <= pivot and i < end:
            i += 1
        
        # Move j to the left while elements are greater than pivot
        while arr[j] > pivot and j > start:
            j -= 1
        
        # If i and j haven't crossed, swap the elements
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place the pivot in its correct position by swapping with element at j
    arr[start], arr[j] = arr[j], arr[start]
    
    # Return the index of the pivot element
    return j


# Driver code to test the QuickSort implementation
if __name__ == "__main__":
    # Example array to be sorted
    arr = [5, 2, 8, 4, 1]
    
    # Call quickSort on the entire array (from index 0 to length-1)
    quickSort(arr, 0, len(arr) - 1)
    
    # Print the sorted array
    print(*arr)

"""
QuickSort Explanation:

QuickSort is a highly efficient divide-and-conquer sorting algorithm. It works by selecting
a 'pivot' element from the array and partitioning the other elements into two sub-arrays,
according to whether they are less than or greater than the pivot. The sub-arrays are then
sorted recursively.

Algorithm Steps:
1. Choose a pivot element from the array
2. Partition the array around the pivot so that:
   - Elements smaller than the pivot come before it
   - Elements greater than the pivot come after it
3. Recursively apply the above steps to the sub-arrays of elements with smaller and larger values

Step-by-Step Visual Representation for array [5, 2, 8, 4, 1]:

Initial Array: [5, 2, 8, 4, 1]

Step 1: First Partition (pivot = 5)
- Compare elements with pivot 5:
  - Elements <= 5: [2, 4, 1]
  - Elements > 5: [8]
- After partitioning: [2, 4, 1, 5, 8]
- Pivot 5 is now at index 3

Step 2: Recursively sort left sub-array [2, 4, 1] (pivot = 2)
- Compare elements with pivot 2:
  - Elements <= 2: [1]
  - Elements > 2: [4]
- After partitioning: [1, 2, 4]
- Pivot 2 is now at index 1

Step 3: Recursively sort right sub-array [4] (only one element, already sorted)

Step 4: Recursively sort right sub-array [8] (only one element, already sorted)

Final Sorted Array: [1, 2, 4, 5, 8]

Detailed Working of Partition Function:
For array [5, 2, 8, 4, 1] with pivot = 5:
1. i=0, j=4: arr[0]=5 > arr[4]=1, so swap -> [1, 2, 8, 4, 5], i=1, j=3
2. i=1, j=3: arr[1]=2 <= 5, so i++, i=2; arr[3]=4 <= 5, so i++, i=3
3. i=3, j=3: arr[3]=4 <= 5, so i++, i=4; now i>j, exit loop
4. Swap pivot with element at j: swap arr[0] with arr[3] -> [4, 2, 8, 1, 5]
5. But this isn't right, let's trace correctly:

Actually, let's retrace with the correct algorithm:
1. Pivot = 5 (first element)
2. i=0, j=4
3. Move i to right while arr[i] <= 5: i moves to index 1 (value 2), then 2 (value 8), stops because 8 > 5
4. Move j to left while arr[j] > 5: j stays at 4 because 1 <= 5
5. Since i < j, swap arr[2] and arr[4]: [5, 2, 1, 4, 8]
6. Continue: i=3, j=3
7. Move i to right while arr[i] <= 5: i moves to index 4 (value 8), stops because 8 > 5
8. Move j to left while arr[j] > 5: j stays at 3 because 4 <= 5
9. Now i > j, exit loop
10. Swap pivot with element at j: swap arr[0] with arr[3]: [4, 2, 1, 5, 8]
11. Return j=3 (position of pivot)

This is how QuickSort partitions the array and recursively sorts the sub-arrays.
"""