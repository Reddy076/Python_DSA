def quickSort(arr,start,end):
    if start>=end:
        return
    partision=func(arr,start,end)
    quickSort(arr,start,partision-1)
    quickSort(arr,partision+1,end)
def func(arr,start,end):
    pivot=arr[start]
    i=start
    j=end
    while(i<j):
        while(arr[i]<=pivot and i<end):
            i+=1
        while(arr[j]>pivot and j>start):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    
    arr[start], arr[j] = arr[j], arr[start]
    return j    





arr = [5, 2, 8, 4, 1]
quickSort(arr, 0, len(arr) - 1)
print(*arr)