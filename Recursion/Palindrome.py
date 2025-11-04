def printArr(arr, n):
    """
    Returns a copy of the array.
    
    Time Complexity: O(n) - We iterate through the array
    Space Complexity: O(n) - For the copied array
    
    Parameters:
    arr (list): The input array
    n (int): The size of the array
    
    Returns:
    list: A copy of the array
    """
    # Return a copy of the array
    return arr[:]


def revArr(arr, start, end):
    """
    Recursively reverses an array in-place using two pointers.
    
    This function swaps elements from both ends of the array and moves toward the center.
    
    Time Complexity: O(n) - We process each element once
    Space Complexity: O(n) - Due to the recursion stack
    
    Parameters:
    arr (list): The array to reverse (modified in-place)
    start (int): Starting index
    end (int): Ending index
    """
    # Base case: If start pointer crosses end pointer, stop recursion
    if start < end:
        # Swap elements at start and end positions
        arr[start], arr[end] = arr[end], arr[start]
        
        # Recursive call with moved pointers
        revArr(arr, start + 1, end - 1)


def isPalindrome(s, left, right):
    """
    Recursively checks if a string is a palindrome using two pointers.
    
    Time Complexity: O(n) - We check each character once
    Space Complexity: O(n) - Due to the recursion stack
    
    Parameters:
    s (str): The string to check
    left (int): Left pointer
    right (int): Right pointer
    
    Returns:
    bool: True if the string is a palindrome, False otherwise
    """
    # On first call, convert string to lowercase for case-insensitive comparison
    if left == 0:
        s = s.lower()
    
    # Base case: If pointers meet or cross, we've checked all characters
    if left >= right:
        return True
    
    # If characters at current positions don't match, it's not a palindrome
    if s[left] != s[right]:
        return False
    
    # Recursive call with moved pointers
    return isPalindrome(s, left + 1, right - 1)


if __name__ == "__main__":
    # Method 1: Reverse array and compare
    str_val = 'AbB'
    split = list(str_val)
    n = len(split)
    
    # Store original array
    first = printArr(split, n)
    
    # Reverse the array
    revArr(split, 0, n - 1)
    
    # Store reversed array
    second = printArr(split, n)
    
    # Compare original and reversed arrays
    if first == second:
        print('"' + str_val + '" is a palindrome')
    else:
        print('"' + str_val + '" is not a palindrome')

    # Method 2: Two-pointer recursive approach
    s = 'ABA'
    n = len(s)
    
    # Check if string is palindrome
    result = isPalindrome(s, 0, n - 1)
    
    if result:
        print('"' + s + '" is a palindrome')
    else:
        print('"' + s + '" is not a palindrome')

"""
Algorithm Explanation:

Method 1: Array Reversal Approach
1. Convert string to character array
2. Store a copy of the original array
3. Reverse the array using recursive two-pointer technique
4. Store a copy of the reversed array
5. Compare original and reversed arrays

Method 2: Direct Recursive Comparison
1. Use two pointers, one at the beginning and one at the end
2. Compare characters at both pointers
3. If they match, move pointers toward each other
4. If they don't match, it's not a palindrome
5. If pointers meet or cross, it's a palindrome

Example Walkthrough for Method 1 with "AbB":
1. Original array: ['A', 'b', 'B']
2. Reversed array: ['B', 'b', 'A']
3. ['A', 'b', 'B'] ≠ ['B', 'b', 'A'], so not a palindrome

Example Walkthrough for Method 2 with "ABA":
1. isPalindrome("ABA", 0, 2):
   - left=0, right=2: 'A' == 'A', so continue
   - isPalindrome("ABA", 1, 1):
     - left=1, right=1: left >= right, so return True
2. Result: True, "ABA" is a palindrome

Time Complexity: O(n) for both methods
Space Complexity: O(n) for both methods due to recursion stack
"""