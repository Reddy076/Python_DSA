def isFibo(N,a=0,b=1):
    if a==N or b==N:
        return True
    if a>N:
        return False
    
    
        
    return isFibo(N,b,a+b)
    
if __name__ == "__main__":
    N=5
    
    if isFibo(N):
        print(f"{N} is a Fibonacci number")
    else:
        print(f"{N} is NOT a Fibonacci number")
        
    print(isFibo(N))
    
    
        
        
# print N fibinochi 


def print_fib_recursive(n, a=0, b=1, series=None):
    if series is None:
        series = []
    
    if a > n:
        print("Fibonacci series up to", n, ":")
        print(" ".join(map(str, series)))
        return
    
    series.append(a)
    print_fib_recursive(n, b, a + b, series)

# Test
n = 50
print_fib_recursive(n)
    
    
    
    
    
    
    
    
   
    
    