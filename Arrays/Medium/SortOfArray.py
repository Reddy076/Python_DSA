def duplicate(arr,n):
  # Dutch National algorithm
    low,mid,high=0,0,n-1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
            
        elif arr[mid]==2:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr

    # Counting Sort Algorithm

def count_sort(arr,n):
    count_0=0
    count_1=0
    count_2=0
    for i in range(n):
        if arr[i]==0:
            count_0+=1
        elif arr[i]==1:
            count_1+=1
        elif arr[i]==2:
            count_2+=1
    for i in range(count_0):
        arr[i]=0
    for i in range(count_0,count_1):
        arr[i]=1
    for i in range(count_1,count_2):
        arr[i]=2
    return arr
    
if __name__ == "__main__":
    arr=[2,0,2,1,1,0]
    n=len(arr)
    x=duplicate(arr,n)
    print(x)