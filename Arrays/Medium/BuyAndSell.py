def duplicate(arr,n):
    # Brute Force
    maxpro=0
    buy_date=-1
    sell_date=-1
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]>arr[i]:
                profit=arr[j]-arr[i]
                if profit>maxpro:
                    maxpro=profit
                    buy_date=i
                    sell_date=j
    return maxpro,buy_date,sell_date
            
            
    

if __name__ == "__main__":
    arr=[7,1,5,3,6,4]
    n=len(arr)
    x=duplicate(arr,n)
    print(x)