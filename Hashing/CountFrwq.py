# Count frequency of each element in the array

def countFreq(arr, n):
    """
    Counts the frequency of each element in the array.
    
    This function iterates through the array and for each element, counts how many times
    it appears in the rest of the array. It uses a visited array to avoid counting
    the same element multiple times.
    
    Time Complexity: O(n^2) - Two nested loops
    Space Complexity: O(n) - For the visited array
    
    Parameters:
    arr (list): The input array
    n (int): The size of the array
    
    Returns:
    None: Prints the frequency of each element directly
    """
    # Create a visited array to track which elements have been counted
    visited = [False] * n
    
    # Iterate through each element in the array
    for i in range(n):
        # If element is already counted, skip it
        if (visited[i] == True):
            continue
        
        # Count the frequency of the current element
        count = 1
        
        # Check the rest of the array for the same element
        for j in range(i + 1, n):
            if (arr[i] == arr[j]):
                # Mark as visited to avoid counting again
                visited[j] = True
                count += 1
        
        # Print the element and its frequency
        print(arr[i], count)


if __name__ == "__main__":
    # Example array
    arr = [10, 5, 10, 15, 10, 5]
    n = len(arr)
    
    # Count and print frequency of each element
    countFreq(arr, n)

"""
Algorithm Explanation:

This algorithm counts the frequency of each element in an array using a brute force approach.

Approach:
1. Create a visited array to track which elements have been counted
2. For each element in the array:
   - If it's already visited, skip it
   - Otherwise, count its frequency by checking all subsequent elements
   - Mark matching elements as visited to avoid counting them again
   - Print the element and its frequency

Example Walkthrough:
For array [10, 5, 10, 15, 10, 5]:
1. i=0, arr[0]=10: Check rest of array for 10s
   - j=1: arr[1]=5 ≠ 10
   - j=2: arr[2]=10 = 10, count=2, visited[2]=True
   - j=3: arr[3]=15 ≠ 10
   - j=4: arr[4]=10 = 10, count=3, visited[4]=True
   - j=5: arr[5]=5 ≠ 10
   - Print: "10 3"

2. i=1, arr[1]=5: Check rest of array for 5s
   - j=2: arr[2]=10 ≠ 5 (and visited[2]=True, but we still check)
   - j=3: arr[3]=15 ≠ 5
   - j=4: arr[4]=10 ≠ 5 (and visited[4]=True)
   - j=5: arr[5]=5 = 5, count=2, visited[5]=True
   - Print: "5 2"

3. i=2, arr[2]=10: visited[2]=True, skip

4. i=3, arr[3]=15: Check rest of array for 15s
   - j=4: arr[4]=10 ≠ 15 (and visited[4]=True)
   - j=5: arr[5]=5 ≠ 15 (and visited[5]=True)
   - Print: "15 1"

5. i=4, arr[4]=10: visited[4]=True, skip

6. i=5, arr[5]=5: visited[5]=True, skip

Final Output:
10 3
5 2
15 1

Note: This is a brute force approach with O(n^2) time complexity. A more efficient
approach would use a hash map/dictionary with O(n) time complexity.
"""