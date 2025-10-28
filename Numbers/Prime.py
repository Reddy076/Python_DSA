# checks the prime number

n = int(input("Enter a number: "))

if n < 2:
    print(f"{n} is NOT prime")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{n} is PRIME")
    else:
        print(f"{n} is NOT prime")

#  list of prime numbers

n = int(input("Enter upper limit: "))

print(f"Prime numbers up to {n}:")
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")