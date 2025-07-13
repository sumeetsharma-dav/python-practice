def fib(a,b,n):
    if n == 0:
        return a
    return fib(b, a+b,n-1)

def fib_1(n):
    if n == 0 or n == 1:
        return n
    return fib_1(n-1) + fib_1(n-2)

print(fib_1(9))


"""
TC = O(2^n)
SC = O(2^n)
"""