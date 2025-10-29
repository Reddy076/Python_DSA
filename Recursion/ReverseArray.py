def printArr(arr,n):
        for i in range(n):
            print(arr[i], end=" ")
        print()
def revArr(arr,start,end):
    if start<end:
        arr[start],arr[end]=arr[end],arr[start]
        revArr(arr,start+1,end-1)
    
            
        



if __name__ == "__main__":
    arr=[1,2,3,4,5]
    n=len(arr)
  
    
    printArr(arr,n)
    
    revArr(arr,0,n-1)
    
    printArr(arr,n)