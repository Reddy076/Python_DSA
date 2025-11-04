def check(arr):
    max_count=0
    count=0
    for i in range(len(arr)):
        if arr[i]==1:
            count+=1
            max_count=max(max_count,count)     
        else:
            count=0
    return max_count
    
            
arr = [1,1,0,1,1,1]
c=check(arr)

print(c)