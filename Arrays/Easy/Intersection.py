def intersection(arr1,arr2):
  #  Brute force
   
    visited=[0]*len(arr2)
    inter=[]
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]==arr2[j] and visited[j]==0:
                inter.append(arr1[i])
                visited[j]=1
                break
            if arr2[j]>arr1[i]:
                break
    return inter

    #  Optimal Approach

    i,j=0,0
    inter=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr1[i]:
            j+=1
        else:
            inter.append(arr1[i])
            i+=1
            j+=1
            
    return inter
    




arr1 = [1,2,3,4,5]
arr2 = [2,3,4,4,5]
inter=intersection(arr1,arr2)

print(inter)