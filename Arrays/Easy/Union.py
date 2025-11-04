def shift(arr1,arr2):


  #   using set

  #   my_set=set()
  #   if not arr1 and arr2:
  #       return 0
  #   for i in range(len(arr1)):
  #       my_set.add(arr1[i])
  #   for j in range(len(arr2)):
  #       my_set.add(arr2[j])


  #  Using two Pointer
    
    i,j=0,0
    union=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            if len(union)==0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
        else:
            if len(union)==0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j+=1
    while i < len(arr1):
        if union[-1]!=arr1[i]:
            union.append(arr1[i])
        i+=1
    while j < len(arr2):
        if union[-1]!=arr2[j]:
            union.append(arr2[j])
        j+=1
        
    return union
arr1 = [1,2,3,4,5]
arr2 = [2,3,4,4,5]
union=shift(arr1,arr2)

print(union)