
def check(arr,k):
    
    # Brute force
    # length=0
    # for i in range(len(arr)):
    #     s=0
    #     for j in range(i,len(arr)):
    #         s+=arr[j]
    #     if s==k:
    #         length=max(length,j-i+1)
    # return length
    
    # Hashing
    # it will work for both positive and negative its the optimal one
   
    # n=len(arr)
    # preSumMap = {}
    # Sum = 0
    # maxLen = 0
    # for i in range(n):
    #     Sum += arr[i]
    #     if Sum == k:
    #         maxLen = max(maxLen, i + 1)
    #     rem = Sum - k
    #     if rem in preSumMap:
    #         length = i - preSumMap[rem]
    #         maxLen = max(maxLen, length)
    #     if Sum not in preSumMap:
    #         preSumMap[Sum] = i

    # return maxLen
    
    # two pointer
    i,j=0,0
    maxe=0
    n=len(arr)
    sum=arr[0]
    while j<n:
        while i<=j and sum >k:
            sum-=arr[i]
            i+=1
        if sum==k:
            maxe=max(maxe,j-i+1)
        j +=1
        if j < n : sum+=arr[j]
    return maxe
    
    


arr = [1,9,2,3,5]
k=10
c=check(arr,k)

print(c)