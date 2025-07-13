"""
1. Sum of first n natural number
2. Factorial of a number
"""


def sumOfN(n):
    if n == 1:
        return 1
    return n + sumOfN(n-1)
def find_factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * find_factorial(n-1)

print(find_factorial(0))

"""
TC = O(N)
SC = O(N)
"""