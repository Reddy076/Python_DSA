# Find the highest/lowest frequency element

def countFreq(arr, n):
    """
    Finds the elements with the highest and lowest frequency in the array.
    
    This function iterates through the array and counts the frequency of each element.
    It keeps track of both the maximum and minimum frequencies and their corresponding elements.
    
    Time Complexity: O(n^2) - Two nested loops
    Space Complexity: O(n) - For the visited array
    
    Parameters:
    arr (list): The input array
    n (int): The size of the array
    
    Returns:
    None: Prints the highest and lowest frequency elements directly
    """
    # Create a visited array to track which elements have been counted
    visited = [False] * n
    
    # Initialize variables to track maximum and minimum frequencies
    maxFreq = 0
    minFreq = n  # Initialize to maximum possible frequency
    maxEle = 0
    minEle = 0
    
    # Iterate through each element in the array
    for i in range(n):
        # If element is already counted, skip it
        if(visited[i] == True):
            continue
        
        # Count the frequency of the current element
        count = 1
        
        # Check the rest of the array for the same element
        for j in range(i + 1, n):
            if(arr[i] == arr[j]):
                visited[j] = True
                count += 1
        
        # Update maximum frequency and element if current count is higher
        if count > maxFreq:    
            maxFreq = count
            maxEle = arr[i]
        
        # Update minimum frequency and element if current count is lower
        if count < minFreq:
            minFreq = count
            minEle = arr[i]
    
    # Print the results
    print("Highest frequency:", maxFreq, "Element:", maxEle)
    print("Lowest frequency:", minFreq, "Element:", minEle)


if __name__ == "__main__":
    # Example array
    arr = [10, 5, 10, 15, 10, 5]
    n = len(arr)
    
    # Find and print highest and lowest frequency elements
    countFreq(arr, n)

"""
Algorithm Explanation:

This algorithm finds the elements with the highest and lowest frequency in an array.

Approach:
1. Create a visited array to track which elements have been counted
2. Initialize variables to track maximum and minimum frequencies
3. For each element in the array:
   - If it's already visited, skip it
   - Otherwise, count its frequency by checking all subsequent elements
   - Mark matching elements as visited to avoid counting them again
   - Update maximum and minimum frequencies and their corresponding elements
4. Print the results

Example Walkthrough:
For array [10, 5, 10, 15, 10, 5]:
1. i=0, arr[0]=10: Count frequency
   - Compare with rest: 10 appears at indices 2 and 4
   - Count = 3
   - maxFreq = 3, maxEle = 10
   - minFreq = 3, minEle = 10

2. i=1, arr[1]=5: Count frequency
   - Compare with rest: 5 appears at index 5
   - Count = 2
   - 2 < maxFreq(3), so no change to max
   - 2 < minFreq(3), so minFreq = 2, minEle = 5

3. i=2, arr[2]=10: visited[2]=True, skip

4. i=3, arr[3]=15: Count frequency
   - Compare with rest: no more 15s
   - Count = 1
   - 1 < maxFreq(3), so no change to max
   - 1 < minFreq(2), so minFreq = 1, minEle = 15

5. i=4, arr[4]=10: visited[4]=True, skip

6. i=5, arr[5]=5: visited[5]=True, skip

Final Results:
- Highest frequency: 3, Element: 10
- Lowest frequency: 1, Element: 15

Note: This is a brute force approach with O(n^2) time complexity. A more efficient
approach would use a hash map/dictionary with O(n) time complexity.
"""