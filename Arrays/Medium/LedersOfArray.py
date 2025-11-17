# Leaders in an Array

# optimal Solution
arr=[10, 22, 12, 3, 0, 6]
n=len(arr)
max=float("-inf")
ans=[]
i=n-1
while i>=0:
    if arr[i]>=max:
        max=arr[i]
        ans.append(arr[i])
    i-=1
ans.reverse()
print(ans)
    
        
        
        

# brute force
# arr=[10, 22, 12, 3, 0, 6]
# n=len(arr)
# ans=[]
# for i in range(n):
#     is_leader=True
#     for j in range(i+1,n):
#         if arr[i]<=arr[j]:
#             is_leader=False
#     if is_leader:
#         # ans.append(arr[i])
#         print(arr[i],end=" ")
# print(ans)