def check(arr):
    # maxe=0
    # for i in range(len(arr)):
    #     maxe=max(maxe,arr[i])
    # hash=[0]*(maxe+1)
    # for i in arr:
    #     hash[i]+=1
    # for num in arr:
    #     if hash[num]==1:
    #         return num
            
    xorr = 0
    for num in arr:
        xorr ^= num
    return xorr
            
arr = [2,2,1]
c=check(arr)

print(c)