def shift(arr,num):
    #  left shift
    if not arr:
        return 0
    
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1
    
    
    return arr 
    

arr = [1,2,0,4,5,0,7]
num=2
k=shift(arr,num)
print(k)