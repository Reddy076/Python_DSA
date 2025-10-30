# Selection Sort
def sort_Arr(arr,n):
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if(arr[j]<arr[mini]):
                mini=j
        temp=arr[mini]
        arr[mini]=arr[i]
        arr[i]=temp
        
    


if __name__ == "__main__":
    arr=[13,46,24,52,20,9]
    n=len(arr)
    sort_Arr(arr,n)
    print(arr)