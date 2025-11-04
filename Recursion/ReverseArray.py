def printArr(arr, n):
    """
    Prints the elements of an array.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i in range(n):
        print(arr[i], end=" ")
    print()


def revArr(arr, start, end):
    """
    Recursively reverses an array in-place using two pointers.
    
    Time Complexity: O(n)
    Space Complexity: O(n) due to recursion stack
    """
    # Base case: If start pointer crosses end pointer, stop recursion
    if start < end:
        # Swap elements at start and end positions
        arr[start], arr[end] = arr[end], arr[start]
        
        # Recursive call with moved pointers
        revArr(arr, start + 1, end - 1)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    
    print("Original array:")
    printArr(arr, n)
    
    # Reverse the array
    revArr(arr, 0, n - 1)
    
    print("Reversed array:")
    printArr(arr, n)