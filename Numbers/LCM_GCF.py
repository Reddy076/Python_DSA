#LCM

n1=12
n2=18
start=max(n1,n2)

for i in range(start,n1*n2+1):
    if(i%n1==0 and i%n2==0):
        print(i)
        break

# GCF

n1=12
n2=18
while n2 !=0:
    n1,n2=n2,n1%n2
    
print(n1)