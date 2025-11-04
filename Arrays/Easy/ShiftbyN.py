def shift(arr, d):


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

    #  Optimal method

    # n = len(arr)
    # d %= n 
    
    # arr[d:]=reversed(arr[d:]) #[::-1]
    # arr[:d]=reversed(arr[:d])
    # arr.reverse()
    # return arr
    """
    Shifts array elements by d positions to the right.
    
    This function performs a right rotation of array elements by d positions.
    For example, if arr = [1,2,3,4,5] and d = 2, the result will be [4,5,1,2,3].
    
    Time Complexity: O(n) - We iterate through the array elements
    Space Complexity: O(d) - We use temporary space to store d elements
    
    Parameters:
    arr (list): The input array to be shifted
    d (int): Number of positions to shift (rotate)
    
    Returns:
    list: The shifted array
    """
    # Handle edge cases
    if not arr:
        return []
    
    n = len(arr)
    # Handle cases where d is greater than array length
    d %= n
    
    # Store the last d elements in a temporary array
    # These will be moved to the beginning after shifting
    temp = arr[n-d:]
    
    # Shift the first (n-d) elements to the right by d positions
    # We iterate backwards to avoid overwriting elements
    for i in range(n-d-1, -1, -1):
        arr[i + d] = arr[i]
    
    # Place the stored elements at the beginning of the array
    for i in range(d):
        arr[i] = temp[i]
    
    return arr


# Driver code to test the shift function
if __name__ == "__main__":
    # Example array
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    
    # Perform right shift by d positions
    shifted_array = shift(arr, d)
    
    # Print the result
    print("Array after right shift by", d, "positions:", shifted_array)

"""
Algorithm Explanation:

This algorithm performs a right rotation of array elements by d positions.

Approach:
1. Store the last d elements in a temporary array (these will move to the front)
2. Shift the first (n-d) elements to the right by d positions
3. Place the stored elements at the beginning of the array

Example Walkthrough:
For array [1, 2, 3, 4, 5, 6, 7] and d = 2:
1. Store last d elements: temp = [6, 7]
2. Shift first (n-d) elements to the right:
   - arr[4] = arr[2] => [1, 2, 3, 4, 3, 6, 7]
   - arr[3] = arr[1] => [1, 2, 3, 2, 3, 6, 7]
   - arr[2] = arr[0] => [1, 2, 1, 2, 3, 6, 7]
3. Place stored elements at the beginning:
   - arr[0] = temp[0] => [6, 2, 1, 2, 3, 6, 7]
   - arr[1] = temp[1] => [6, 7, 1, 2, 3, 6, 7]

Wait, let's trace this correctly:
1. Original array: [1, 2, 3, 4, 5, 6, 7]
2. temp = arr[5:7] = [6, 7] (last 2 elements)
3. Shift first 5 elements right by 2 positions (backwards iteration):
   - i=4: arr[6] = arr[4] => [1, 2, 3, 4, 5, 6, 5]
   - i=3: arr[5] = arr[3] => [1, 2, 3, 4, 5, 4, 5]
   - i=2: arr[4] = arr[2] => [1, 2, 3, 4, 3, 4, 5]
   - i=1: arr[3] = arr[1] => [1, 2, 3, 2, 3, 4, 5]
   - i=0: arr[2] = arr[0] => [1, 2, 1, 2, 3, 4, 5]
4. Place temp elements at beginning:
   - arr[0] = temp[0] = 6 => [6, 2, 1, 2, 3, 4, 5]
   - arr[1] = temp[1] = 7 => [6, 7, 1, 2, 3, 4, 5]

Actually, that's not right either. Let me trace again:
1. Original array: [1, 2, 3, 4, 5, 6, 7]
2. temp = arr[5:7] = [6, 7]
3. Shift first 5 elements right by 2 positions:
   - i=4: arr[6] = arr[4] => [1, 2, 3, 4, 5, 6, 5]
   - i=3: arr[5] = arr[3] => [1, 2, 3, 4, 5, 4, 5]
   - i=2: arr[4] = arr[2] => [1, 2, 3, 4, 3, 4, 5]
   - i=1: arr[3] = arr[1] => [1, 2, 3, 2, 3, 4, 5]
   - i=0: arr[2] = arr[0] => [1, 2, 1, 2, 3, 4, 5]
4. Place temp elements at beginning:
   - arr[0] = temp[0] = 6 => [6, 2, 1, 2, 3, 4, 5]
   - arr[1] = temp[1] = 7 => [6, 7, 1, 2, 3, 4, 5]

Hmm, there's an issue with my tracing. Let me look at the actual result:
The expected result should be [6, 7, 1, 2, 3, 4, 5] which is correct for a right shift by 2.

The algorithm works as follows:
1. Store the last d elements that will wrap around to the front
2. Shift all other elements to the right
3. Place the stored elements at the beginning
"""