# Selection Sort
def sort_Arr(arr, n):
    """
    Sorts an array using the Selection Sort algorithm.
    
    Selection Sort repeatedly finds the minimum element from the unsorted part 
    of the array and puts it at the beginning. It maintains two subarrays:
    1. The sorted subarray which is built up from left to right
    2. The remaining unsorted subarray
    
    Time Complexity: O(n^2) in all cases (best, average, worst)
    Space Complexity: O(1) - Sorting is done in-place
    
    Parameters:
    arr (list): The array to be sorted
    n (int): The size of the array
    
    Returns:
    list: The sorted array
    """
    # Traverse through all array elements
    for i in range(n-1):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        
        # Check the rest of the array for a smaller element
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


if __name__ == "__main__":
    # Test selection sort
    arr = [13, 46, 24, 52, 20, 9]
    n = len(arr)
    
    print("Original array:", arr)
    
    # Sort the array
    sort_Arr(arr, n)
    
    print("Sorted array:", arr)

"""
Algorithm Explanation:

Selection Sort works by repeatedly finding the minimum element from the unsorted 
part of the array and putting it at the beginning.

Approach:
1. Find the minimum element in the entire array and swap it with the first element
2. Find the minimum element in the remaining unsorted array and swap it with the second element
3. Continue this process for the entire array

Example Walkthrough for [13, 46, 24, 52, 20, 9]:

Initial: [13, 46, 24, 52, 20, 9]

Step 1 (i=0):
- Find minimum in [13, 46, 24, 52, 20, 9]: min=9 at index 5
- Swap arr[0] and arr[5]: [9, 46, 24, 52, 20, 13]

Step 2 (i=1):
- Find minimum in [46, 24, 52, 20, 13]: min=13 at index 4
- Swap arr[1] and arr[4]: [9, 13, 24, 52, 20, 46]

Step 3 (i=2):
- Find minimum in [24, 52, 20, 46]: min=20 at index 3
- Swap arr[2] and arr[3]: [9, 13, 20, 52, 24, 46]

Step 4 (i=3):
- Find minimum in [52, 24, 46]: min=24 at index 4
- Swap arr[3] and arr[4]: [9, 13, 20, 24, 52, 46]

Step 5 (i=4):
- Find minimum in [52, 46]: min=46 at index 5
- Swap arr[4] and arr[5]: [9, 13, 20, 24, 46, 52]

Final Sorted Array: [9, 13, 20, 24, 46, 52]

Time Complexity: O(n^2) in all cases
- Outer loop runs n-1 times
- Inner loop runs (n-1) + (n-2) + ... + 1 = n(n-1)/2 times

Space Complexity: O(1) - Only uses a constant amount of extra space

Note: Selection Sort is not stable (doesn't preserve the relative order of equal elements)
and performs poorly on large lists compared to more advanced algorithms.
"""