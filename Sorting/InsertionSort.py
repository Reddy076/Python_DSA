# Insertion Sort
def sort_Arr(arr, n):
    """
    Sorts an array using the Insertion Sort algorithm (Iterative approach).
    
    Insertion Sort builds the final sorted array one item at a time. It works 
    similarly to how we sort playing cards in our hands. We start with the 
    second element and insert it into the correct position in the sorted part 
    of the array (elements before it).
    
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
    # Traverse from the second element to the last element
    for i in range(1, n):
        # Store the current element to be inserted
        key = arr[i]
        # Start comparing with the element just before the current element
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than key
        # one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key at its correct position
        arr[j + 1] = key
    
    return arr


# Insertion Sort - Recursive Version
def sort_Arr_recursive(arr, n, i=1):
    """
    Sorts an array using the Insertion Sort algorithm (Recursive approach).
    
    Time Complexity: O(n^2)
    Space Complexity: O(n) - Due to recursion stack
    
    Parameters:
    arr (list): The array to be sorted (modified in-place)
    n (int): The size of the array
    i (int): Current index being processed (default 1)
    
    Returns:
    list: The sorted array
    """
    # Base case: if i reaches n, sorting is done
    if i >= n:
        return arr
    
    # Store the current element to be inserted
    key = arr[i]
    # Start comparing with the element just before the current element
    j = i - 1
    
    # Move elements that are greater than key one position ahead
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    
    # Insert the key at its correct position
    arr[j + 1] = key
    
    # Recursive call: move to next element
    return sort_Arr_recursive(arr, n, i + 1)


if __name__ == "__main__":
    # Test iterative insertion sort
    arr1 = [13, 46, 24, 52, 20, 9]
    n = len(arr1)
    print("Original array:", arr1)
    
    # Sort using iterative approach
    sort_Arr(arr1, n)
    print("Sorted array (iterative):", arr1)
    
    # Test recursive insertion sort
    arr2 = [13, 46, 24, 52, 20, 9]
    print("\nOriginal array:", arr2)
    
    # Sort using recursive approach
    sort_Arr_recursive(arr2, n)
    print("Sorted array (recursive):", arr2)

"""
Algorithm Explanation:

Insertion Sort works similarly to how we sort playing cards in our hands.

Approach:
1. Start with the second element (index 1)
2. Compare it with elements in the sorted portion (elements before it)
3. Shift larger elements one position to the right
4. Insert the current element at its correct position
5. Repeat for all elements

Example Walkthrough for [13, 46, 24, 52, 20, 9]:

Initial: [13, 46, 24, 52, 20, 9]
- 13 is considered sorted

Step 1 (i=1, key=46):
- Compare 46 with 13: 46 > 13, so no shift needed
- Insert 46 at position 1: [13, 46, 24, 52, 20, 9]

Step 2 (i=2, key=24):
- Compare 24 with 46: 24 < 46, shift 46 right: [13, 46, 46, 52, 20, 9]
- Compare 24 with 13: 24 > 13, so stop
- Insert 24 at position 1: [13, 24, 46, 52, 20, 9]

Step 3 (i=3, key=52):
- Compare 52 with 46: 52 > 46, so no shift needed
- Insert 52 at position 3: [13, 24, 46, 52, 20, 9]

Step 4 (i=4, key=20):
- Compare 20 with 52: 20 < 52, shift 52 right: [13, 24, 46, 52, 52, 9]
- Compare 20 with 46: 20 < 46, shift 46 right: [13, 24, 46, 46, 52, 9]
- Compare 20 with 24: 20 < 24, shift 24 right: [13, 24, 24, 46, 52, 9]
- Compare 20 with 13: 20 > 13, so stop
- Insert 20 at position 1: [13, 20, 24, 46, 52, 9]

Step 5 (i=5, key=9):
- Compare 9 with 52: 9 < 52, shift 52 right: [13, 20, 24, 46, 52, 52]
- Compare 9 with 46: 9 < 46, shift 46 right: [13, 20, 24, 46, 46, 52]
- Compare 9 with 24: 9 < 24, shift 24 right: [13, 20, 24, 24, 46, 52]
- Compare 9 with 20: 9 < 20, shift 20 right: [13, 20, 20, 24, 46, 52]
- Compare 9 with 13: 9 < 13, shift 13 right: [13, 13, 20, 24, 46, 52]
- Insert 9 at position 0: [9, 13, 20, 24, 46, 52]

Final Sorted Array: [9, 13, 20, 24, 46, 52]

Time Complexity:
- Best Case: O(n) - When array is already sorted
- Average/Worst Case: O(n^2)

Space Complexity: O(1) for iterative, O(n) for recursive
"""