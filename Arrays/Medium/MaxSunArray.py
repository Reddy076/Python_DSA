def duplicate(arr,n):
    
    
    # brute force
    maxi = float('-inf')
    start_idx=-1
    end_idx=-1
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if sum>maxi:
                maxi=sum
                start_idx = i
                end_idx = j
            
    return maxi,start_idx,end_idx
    
            

if __name__ == "__main__":
    arr=[-2,1,-3,4,-1,2,1,-5,4]
    n=len(arr)
    x=duplicate(arr,n)
    print(x)