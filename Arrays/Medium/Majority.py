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
    
        
            
    
if __name__ == "__main__":
    arr=[3,2,3]
    n=len(arr)
    x=duplicate(arr,n)
    print(x)