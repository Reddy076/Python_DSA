# set matrix zeros
# brute Force

# def markRow(arr,n,m,i):
#     for j in range(m):
#         if arr[i][j]!=0:
#             arr[i][j]=-1
# def markCol(arr,n,m,j):
#     for i in range(n):
#         if arr[i][j]!=0:
#             arr[i][j]=-1
# def mark(arr,n,m):
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j]==0:
#                 markRow(arr,n,m,i)
#                 markCol(arr,n,m,j)
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j]==-1:
#                 arr[i][j]=0
#     return arr

# Better

# def mark(arr,n,m):
#     row=[0]*n
#     col=[0]*m
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j]==0:
#                 row[i]=1
#                 col[j]=1
#     for i in range(n):
#         for j in range(m):
#             if row[i]==1 or col[j]==1:
#                 arr[i][j]=0
#     return arr

def mark(arr,n,m):
    # row=[0]*n
    # col=[0]*m
    col0=1
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                arr[i][0]=0
                if j!=0:
                    arr[0][j]=0
                else:
                    col0=0
    for i in range(1,n):
        for j in range(1,m):
            if arr[i][j]!=0:
                if arr[i][0]==0 or arr[0][j]==0:
                    arr[i][j]=0
    if arr[0][0]==0:
        for j in range(m):
            arr[0][j]
    if col0==0:
        for i in range(n):
            arr[i][0]=0
    return arr



arr=[[1,1,1],[1,0,1],[1,1,1]]
n=len(arr)
m=len(arr[0])
ans=mark(arr,n,m)
print(ans)