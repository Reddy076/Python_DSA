def check(arr,N):
    # Brute force
    
    # for i in range(1,N+1):
    #     flag=0
    #     for j in range(len(arr)):
    #         if arr[j]==i:
    #             flag=1
    #             break
    #     if(flag==0):
    #         return i
    # return -1
    
    # #  Hashing
    
    #  visited=[0]*(N+1)
    # for i in arr:
    #     # if 1<= i <=N:
    #     visited[i]=1
    # for j in range(1,N+1):
    #     if visited[j]==0:
    #         return j
    # return -1
    
    # Summation
    
    # sum=(N*(N+1))/2
    # sum1=0
    
    # for i in range(len(arr)):
    #     sum1+=arr[i]
    # return sum-sum1
    
    # XOR
    XOR1=0
    for n in range(1,N+1):
        XOR1=XOR1^n
    XOR2=0
        
    for i in range(len(arr)):
        XOR2=XOR2^arr[i]
        
    return XOR1 ^ XOR2
   
            
arr = [1,2,4,5]
N=5
c=check(arr,N)

print(c)