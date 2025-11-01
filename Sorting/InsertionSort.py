# Insertion Sort
def sort_Arrr(arr,n):
    for i in range(1,n):
        j=i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    return arr
        
        
        
    


if __name__ == "__main__":
    arr=[13,46,24,52,20,9]
    n=len(arr)
    sort_Arrr(arr,n)
    print(arr)



# Recursion


# Insertion Sort - Recursive Version
def sort_Arr(arr, n, i=1):
    # Base case: if i reaches n, sorting is done
    if i >= n:
        return arr
    
    # Take current element
    j = i
    # Shift larger elements to the right
    while j > 0 and arr[j-1] > arr[j]:
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j -= 1
    
    # Recursive call: move to next element
    return sort_Arr(arr, n, i + 1)


# Driver code
if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    n = len(arr)
    sort_Arr(arr, n)        
    print(arr)