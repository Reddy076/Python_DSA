def duplicate(arr,n,t):
    i=0
    while i<n:
        j=0
        while j<n:
            if i!=j and arr[i]+arr[j]==t:
                # print (arr[i] ,arr[j])
                return arr[i],arr[j]
            j+=1
        i+=1
    return -1,-1
        
    
    
    
if __name__ == "__main__":
    arr=[2,6,5,8,11]
    n=len(arr)
    target=14
    x=duplicate(arr,n,target)
    print(x)