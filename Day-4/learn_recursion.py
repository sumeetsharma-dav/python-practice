"""
Recursion is when a function calls itself
"""

# Let's print hello 4 times to understand recusrion
# HEAD RECURSION
count = 0
def greet():
    global count
    if count == 4:
        return
    print(f"hello recursion number {count}")
    count += 1
    greet()

greet()

# TAIL RECURSION
count1 = 0
def greet1():
    global count1
    if count1 == 4:
        return
    count1 += 1
    greet1()
    print(f"hello recursion number {count1}")

greet1()

"""
TC = O(N+1)
SC = O(N+1)
"""