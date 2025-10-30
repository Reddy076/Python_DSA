# Insertion Sort
def sort_Arr(arr,n):
    for i in range(1,n):
        j=i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    return arr
        
        
        
    


if __name__ == "__main__":
    arr=[13,46,24,52,20,9]
    n=len(arr)
    sort_Arr(arr,n)
    print(arr)