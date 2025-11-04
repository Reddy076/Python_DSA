def shift(arr):
    #  left shift
    if not arr:
        return 0
    n=len(arr)
    temp = []
    for i in range(n):
        if arr[i] !=0:
            temp.append(arr[i])
    for i in range(len(temp)):
        arr[i] = temp[i]
    for i in range(len(temp), len(arr)):
        arr[i] = 0
    
    return arr 
    

arr = [1,2,0,4,5,0,7]
k=shift(arr)
print(k)