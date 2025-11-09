def duplicate(arr,n):
    # Kadane's Algorithm
    
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
    
    # Kadane's Algorithm
    
    maxie=float("-inf")
    sum=0
    ans_start=-1
    ans_end=-1
    for i in range(n):
        if sum==0:
            start=i
        sum+=arr[i]
        if sum>maxie:
            maxie=sum
            ans_short,ans_end=start,i
        if sum<0:
            sum=0
    if maxie<0:
        maxie=0
    return maxie,ans_short,ans_end
            

if __name__ == "__main__":
    arr=[-2,1,-3,4,-1,2,1,-5,4]
    n=len(arr)
    x=duplicate(arr,n)
    print(x)