def duplicate(arr,n):
    # Dutch National algorithm
    ha={}
    for i in range(n):
        if arr[i] not in ha:
            ha[arr[i]]=1
        else:
            ha[arr[i]]+=1
    i=n//2
    for num,cnt in ha.items():
        if cnt>=i:
            return num,cnt

    # Moore's Voting Algorithm
    cnt=0
    ele=None
    for i in range(n):
        if (cnt==0):
            cnt=1
            ele=arr[i]
        
        elif ele==arr[i]:
            cnt+=1
        else:
            cnt-=1
    
    cnt1=0
    for j in range(n):
        if arr[i]==ele:
            cnt1+=1
    if cnt1>(n/2):
        return ele
    return -1
    
        
            
    
if __name__ == "__main__":
    arr=[3,2,3]
    n=len(arr)
    x=duplicate(arr,n)
    print(x)