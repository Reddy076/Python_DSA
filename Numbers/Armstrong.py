num = int(input("Enter a number: "))
original = num
digits = len(str(num))
sum_power = 0

while num > 0:
    digit = num % 10
    sum_power += digit ** digits
    num = num // 10

if sum_power == original:
    print(f"{original} is an Armstrong number!")
else:
    print(f"{original} is NOT an Armstrong number.")