# Bubble Sort
def sort_Arr(arr, n):
    """
    Sorts an array using the Bubble Sort algorithm (Iterative approach).
    
    Bubble Sort repeatedly steps through the list, compares adjacent elements 
    and swaps them if they are in the wrong order. The pass through the list 
    is repeated until the list is sorted.
    
    Time Complexity: 
    - Best Case: O(n) - When array is already sorted
    - Average/Worst Case: O(n^2)
    
    Space Complexity: O(1) - Sorting is done in-place
    
    Parameters:
    arr (list): The array to be sorted
    n (int): The size of the array
    
    Returns:
    list: The sorted array
    """
    # Traverse from the end of the array to the beginning
    for i in range(n-1, 0, -1):
        # In each pass, the largest element "bubbles up" to its correct position
        for j in range(i):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr


def bubble_sort(arr, n=None):
    """
    Sorts an array using the Bubble Sort algorithm (Recursive approach).
    
    Time Complexity: O(n^2)
    Space Complexity: O(n) - Due to recursion stack
    
    Parameters:
    arr (list): The array to be sorted (modified in-place)
    n (int): The size of the unsorted portion of the array
    
    Returns:
    list: The sorted array
    """
    # On first call, set n to the length of the array
    if n is None:
        n = len(arr)

    # Base case: If there's only one element or none, it's already sorted
    if n <= 1:
        return arr

    # One pass: push the largest element to the end
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            # Swap adjacent elements if they are in the wrong order
            arr[j], arr[j+1] = arr[j+1], arr[j]

    # Recurse on the smaller sub-array (last element is now in place)
    return bubble_sort(arr, n-1)


if __name__ == "__main__":
    # Test iterative bubble sort
    arr1 = [13, 46, 24, 52, 20, 9]
    n = len(arr1)
    print("Original array:", arr1)
    
    # Sort using iterative approach
    sort_Arr(arr1, n)
    print("Sorted array (iterative):", arr1)
    
    # Test recursive bubble sort
    arr2 = [13, 46, 24, 52, 20, 9]
    print("\nOriginal array:", arr2)
    
    # Sort using recursive approach
    bubble_sort(arr2)
    print("Sorted array (recursive):", arr2)

"""
Algorithm Explanation:

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements and swaps them if they are in the wrong order.

Approach:
1. Compare adjacent elements in the array
2. If they are in the wrong order, swap them
3. Continue this process for the entire array
4. After each pass, the largest element "bubbles up" to its correct position
5. Repeat until no more swaps are needed

Example Walkthrough for [13, 46, 24, 52, 20, 9]:

Pass 1:
- Compare 13,46: No swap -> [13, 46, 24, 52, 20, 9]
- Compare 46,24: Swap -> [13, 24, 46, 52, 20, 9]
- Compare 46,52: No swap -> [13, 24, 46, 52, 20, 9]
- Compare 52,20: Swap -> [13, 24, 46, 20, 52, 9]
- Compare 52,9: Swap -> [13, 24, 46, 20, 9, 52]
After Pass 1, 52 (largest) is in correct position.

Pass 2:
- Compare 13,24: No swap -> [13, 24, 46, 20, 9, 52]
- Compare 24,46: No swap -> [13, 24, 46, 20, 9, 52]
- Compare 46,20: Swap -> [13, 24, 20, 46, 9, 52]
- Compare 46,9: Swap -> [13, 24, 20, 9, 46, 52]
After Pass 2, 46 (second largest) is in correct position.

Continue this process until the array is fully sorted:
[9, 13, 20, 24, 46, 52]

Time Complexity:
- Best Case: O(n) - When array is already sorted (with optimization)
- Average/Worst Case: O(n^2)

Space Complexity: O(1) for iterative, O(n) for recursive
"""