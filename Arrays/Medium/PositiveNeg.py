# arrange the the array with positive and negative alternative

# similar problem
arr=[1,2,-4,-5,3,4]
n=len(arr)
pos=[]
neg=[]

for i in range(n):
    if arr[i]<0:
        neg.append(arr[i])
    else:
        pos.append(arr[i])
length=min(len(pos),len(neg))
for i in range(length):
    arr[2*i]=pos[i]
    arr[2*i+1]=neg[i]
ind=2*length
for i in range(length,len(pos)):
    arr[ind]=pos[i]
    ind+=1
for i in range(length,len(neg)):
    arr[ind]=neg[i]
    ind+=1
print(arr)
    







# optimal approach
# arr=[1,2,-3,-4]
# n=len(arr)
# ans=[0]*n
# pos,neg=0,1

# for i in range(n):
#     if arr[i] <0:
#         ans[neg]=arr[i]
#         neg+=2
#     else:
#         ans[pos]=arr[i]
#         pos+=2
# print(ans)

# brute force

# arr=[1,2,-3,-4]
# n=len(arr)
# pos=[]
# neg=[]
# for i in range(n):
#     if arr[i]<0:
#         neg.append(arr[i])
#     else:
#         pos.append(arr[i])
# for i in range(n//2):
#     arr[2*i]=pos[i]
#     arr[2*i+1]=neg[i]
# print(arr)
