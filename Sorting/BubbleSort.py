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