# Bubble Sort
def sort_Arr(arr,n):
    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr 
        
        
    


if __name__ == "__main__":
    arr=[13,46,24,52,20,9]
    n=len(arr)
    sort_Arr(arr,n)
    print(arr)


# recurssion

def bubble_sort(arr, n=None):
    if n is None:                # first call – set n = length
        n = len(arr)

    if n <= 1:                   # base case: nothing to sort
        return arr

    # One pass: push the largest element to the end
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

    # Recurse on the *smaller* sub-array (last element is now in place)
    return bubble_sort(arr, n-1)



if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    bubble_sort(arr)
    print(arr)                   