def printArr(arr,n):
        for i in range(n):
        #     print(arr[i], end=" ")
        # print()
            return arr[:]
def revArr(arr,start,end):
    if start<end:
        arr[start],arr[end]=arr[end],arr[start]
        revArr(arr,start+1,end-1)
if __name__ == "__main__":
    str='AbB'
    split=list(str)
    n=len(split)
    
    first =printArr(split,n)
    revArr(split,0,n-1)
    second=printArr(split,n)
    
    if first==second:
        print('is palendrome')
    else:
        print('is not')



# Another Method Using Two Pointers


def isPalendrome(s,left,right):
    if left==0:
        s=s.lower()
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
        
    return isPalendrome(s,left+1,right-1)
    
if __name__ == "__main__":
    s='ABA'
    n=len(s)
    
    print(isPalendrome(s,0,n-1))