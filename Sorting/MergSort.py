class Solution:
    """
    A class to implement the merge sort algorithm.
    Merge sort is a divide-and-conquer algorithm that divides the array into halves,
    recursively sorts each half, and then merges them back together.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    
    # Function to merge two sorted halves of an array
    def merge(self, arr, low, mid, high):
        """
        Merges two sorted subarrays arr[low...mid] and arr[mid+1...high] 
        into a single sorted subarray arr[low...high]
        
        Parameters:
        arr (list): The original array
        low (int): Starting index of the first subarray
        mid (int): Ending index of the first subarray
        high (int): Ending index of the second subarray
        """
        # Create a temporary array to store merged elements
        temp = []
        # Initialize pointers for left and right subarrays
        left, right = low, mid + 1

        # Compare elements from both subarrays and merge in sorted order
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        # Add remaining elements from the left subarray (if any)
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # Add remaining elements from the right subarray (if any)
        while right <= high:
            temp.append(arr[right])
            right += 1

        # Copy the merged elements back to the original array
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    # Recursive function to implement merge sort
    def mergeSort(self, arr, low, high):
        """
        Recursively divides the array into two halves, sorts them,
        and merges them back together.
        
        Parameters:
        arr (list): The array to be sorted
        low (int): Starting index of the array segment
        high (int): Ending index of the array segment
        """
        # Base case: If the segment has only one element or is empty, it's already sorted
        if low >= high:
            return
            
        # Find the middle point to divide the array into two halves
        mid = (low + high) // 2
        
        # Recursively sort the first half (low to mid)
        self.mergeSort(arr, low, mid)
        
        # Recursively sort the second half (mid+1 to high)
        self.mergeSort(arr, mid + 1, high)
        
        # Merge the sorted halves
        self.merge(arr, low, mid, high)


# Driver code to test the merge sort implementation
if __name__ == "__main__":
    # Example array to be sorted
    arr = [5, 2, 8, 4, 1]
    
    # Create an instance of the Solution class
    sol = Solution()
    
    # Call mergeSort on the entire array (from index 0 to length-1)
    sol.mergeSort(arr, 0, len(arr) - 1)
    
    # Print the sorted array
    print(*arr)

"""
Merge Sort Explanation:

Merge sort is a divide-and-conquer algorithm that works by recursively dividing an array 
into smaller subarrays, sorting those subarrays, and then merging them back together.

Algorithm Steps:
1. Divide: Split the array into two halves
2. Conquer: Recursively sort both halves
3. Combine: Merge the two sorted halves to produce a single sorted array

Time Complexity: O(n log n) in all cases (best, average, and worst)
Space Complexity: O(n) for the temporary arrays used during merging

Step-by-Step Visual Representation for array [5, 2, 8, 4, 1]:

Initial Array: [5, 2, 8, 4, 1]

Step 1: Divide
                  [5, 2, 8, 4, 1]
                 /               \
           [5, 2, 8]           [4, 1]
          /         \         /       \
      [5, 2]       [8]     [4]       [1]
     /      \      
   [5]      [2]    

Step 2: Sort and Merge
   [5]      [2]    ->    [2, 5]     [8]     [4]     [1]
     \      /             \         /         \       /
    [2, 5]  [8]    ->    [2, 5, 8]           [1, 4]
          \                   \                 /
         [2, 5, 8]         [1, 4]      ->    [1, 2, 4, 5, 8]

Final Sorted Array: [1, 2, 4, 5, 8]

Detailed Working of Merge Function:
Let's trace through merging [2, 5] and [8]:
1. Compare 2 and 8: 2 is smaller, so add 2 to result
2. Compare 5 and 8: 5 is smaller, so add 5 to result
3. Left array exhausted, add remaining element 8
Result: [2, 5, 8]

Similarly, for merging [4] and [1]:
1. Compare 4 and 1: 1 is smaller, so add 1 to result
2. Right array exhausted, add remaining element 4
Result: [1, 4]

Finally, merging [2, 5, 8] and [1, 4]:
1. Compare 2 and 1: 1 is smaller, so add 1 to result -> [1]
2. Compare 2 and 4: 2 is smaller, so add 2 to result -> [1, 2]
3. Compare 5 and 4: 4 is smaller, so add 4 to result -> [1, 2, 4]
4. Compare 5 and 8: 5 is smaller, so add 5 to result -> [1, 2, 4, 5]
5. Left array exhausted, add remaining element 8 -> [1, 2, 4, 5, 8]

This is how merge sort works - continuously dividing the problem into smaller parts,
sorting them, and merging them back together to form the final sorted array.
"""