# Find the highest/lowest frequency element

def countFreq(arr, n):
    l=[False]*n
    maxFreq = 0
    minFreq = n
    maxEle = 0
    minEle = 0
    for i in range(n):
        if(l[i]==True):
            continue
        count=1
        for j in range(i+1,n):
            if(arr[i]==arr[j]):
                l[j]=True
                count+=1
                
        if count>maxFreq:    
            maxFreq = count
            maxEle = arr[i]

        if count < minFreq:
            minFreq = count
            minEle = arr[i]
            
    print(maxFreq,maxEle)
    print(minFreq,minEle)

if __name__ == "__main__":
    arr = [10,5,10,15,10,5]
    n = len(arr)
    countFreq(arr, n)