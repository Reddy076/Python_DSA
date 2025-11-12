def isFibo(N, a=0, b=1):
    """
    Recursively checks if a number is part of the Fibonacci sequence.
    
    The Fibonacci sequence is a series of numbers where each number is the sum 
    of the two preceding ones, usually starting with 0 and 1.
    
    Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    
    Time Complexity: O(log N) - Related to the golden ratio
    Space Complexity: O(log N) - Due to the recursion stack
    
    Parameters:
    N (int): The number to check
    a (int): First Fibonacci number in current pair (default 0)
    b (int): Second Fibonacci number in current pair (default 1)
    
    Returns:
    bool: True if N is a Fibonacci number, False otherwise
    """
    # Base case: If either a or b equals N, then N is a Fibonacci number
    if a == N or b == N:
        return True
    
    # Base case: If a exceeds N, then N is not a Fibonacci number
    if a > N:
        return False
    
    # Recursive case: Check with the next pair of Fibonacci numbers
    return isFibo(N, b, a + b)


def print_fib_recursive(n, a=0, b=1, series=None):
    """
    Recursively prints the Fibonacci series up to a given number.
    
    Time Complexity: O(F) where F is the count of Fibonacci numbers <= n
    Space Complexity: O(F) due to recursion stack and series list
    
    Parameters:
    n (int): The upper limit for Fibonacci numbers
    a (int): Current Fibonacci number (default 0)
    b (int): Next Fibonacci number (default 1)
    series (list): List to store Fibonacci numbers (default None)
    """
    # Initialize the series list on first call
    if series is None:
        series = []
    
    # Base case: If current Fibonacci number exceeds n, print the series
    if a > n:
        print("Fibonacci series up to", n, ":")
        print(" ".join(map(str, series)))
        return
    
    # Add current Fibonacci number to the series
    series.append(a)
    
    # Recursive call with next pair of Fibonacci numbers
    print_fib_recursive(n, b, a + b, series)


if __name__ == "__main__":
    # Check if a number is a Fibonacci number
    N = 5
    
    if isFibo(N):
        print(f"{N} is a Fibonacci number")
    else:
        print(f"{N} is NOT a Fibonacci number")
    
    print("Result:", isFibo(N))
    
    # Print Fibonacci series up to a number
    n = 50
    print_fib_recursive(n)

"""
Algorithm Explanation:

1. isFibo Function:
   This function checks if a number is part of the Fibonacci sequence using recursion.
   
   Approach:
   - Start with the first two Fibonacci numbers: a=0, b=1
   - If either a or b equals N, then N is a Fibonacci number
   - If a exceeds N, then N is not a Fibonacci number
   - Otherwise, recursively check with the next pair: b and a+b
   
   Example Walkthrough for N=5:
   1. isFibo(5, 0, 1): 0≠5, 1≠5, 0<5, so call isFibo(5, 1, 1)
   2. isFibo(5, 1, 1): 1≠5, 1≠5, 1<5, so call isFibo(5, 1, 2)
   3. isFibo(5, 1, 2): 1≠5, 2≠5, 1<5, so call isFibo(5, 2, 3)
   4. isFibo(5, 2, 3): 2≠5, 3≠5, 2<5, so call isFibo(5, 3, 5)
   5. isFibo(5, 3, 5): 3≠5, but 5==5, so return True
   
   Result: 5 is a Fibonacci number

2. print_fib_recursive Function:
   This function prints all Fibonacci numbers up to a given limit using recursion.
   
   Approach:
   - Start with the first two Fibonacci numbers: a=0, b=1
   - If a exceeds the limit n, print the collected series
   - Otherwise, add a to the series and recursively call with b and a+b
   
   Example Walkthrough for n=10:
   1. print_fib_recursive(10, 0, 1, []): 0≤10, add 0, call with (10, 1, 1, [0])
   2. print_fib_recursive(10, 1, 1, [0]): 1≤10, add 1, call with (10, 1, 2, [0,1])
   3. print_fib_recursive(10, 1, 2, [0,1]): 1≤10, add 1, call with (10, 2, 3, [0,1,1])
   4. print_fib_recursive(10, 2, 3, [0,1,1]): 2≤10, add 2, call with (10, 3, 5, [0,1,1,2])
   5. print_fib_recursive(10, 3, 5, [0,1,1,2]): 3≤10, add 3, call with (10, 5, 8, [0,1,1,2,3])
   6. print_fib_recursive(10, 5, 8, [0,1,1,2,3]): 5≤10, add 5, call with (10, 8, 13, [0,1,1,2,3,5])
   7. print_fib_recursive(10, 8, 13, [0,1,1,2,3,5]): 8≤10, add 8, call with (10, 13, 21, [0,1,1,2,3,5,8])
   8. print_fib_recursive(10, 13, 21, [0,1,1,2,3,5,8]): 13>10, print series [0,1,1,2,3,5,8]
   
   Output: Fibonacci series up to 10: 0 1 1 2 3 5 8
"""




def re(n,a=0,b=1,series=None):
    if series is None:
        series=[]
    if a>n:
        print(" ".join(map(str,series)))
        return
    series.append(a)
    return re(n,b,a+b,series)
        
    
    
    
    
    
n=5
ans=re(n)
print(ans)