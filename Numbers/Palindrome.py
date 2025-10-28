n=454
palindrome=n
rev=0
while(n>0):
    c=n%10
    if c==0:continue
    rev=rev*10+c
    n//=10
print(rev)
if rev==palindrome:print('it is palandrome')
if rev!=palindrome:print ('it is not a palandrome')