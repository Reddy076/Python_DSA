# Optimal Approach

import math 

n=int(input("Enter the number of elements:"))


count=int((math.log10(n)+1))

print("Number of digits:",count)


# bruit force

n=int(input("Enter the number of elements:"))

count=len(list(map(int,str(n))))
print("Number of digits:",count)


# Using lambds

n=int(input("Enter the number of elements:"))

count=sum(map(lambda x:1,str(n)))
print("Number of digits:",count)
