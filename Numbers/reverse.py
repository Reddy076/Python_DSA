# Reverse a number

n=125456
rev=0
while(n>0):
    c=n%10
    rev=rev*10+c
    n//=10
        
print (rev)
