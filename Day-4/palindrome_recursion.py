def palindrome(s):
    l = 0
    r = len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True



def palindrome_recursion(l,r,s):
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return palindrome_recursion(l+1,r-1,s)

print(palindrome_recursion(0,5,"nitina"))
s = "abccbxba"
print(palindrome_recursion(0, len(s)-1, s))
print(palindrome_recursion(0, 4, "nitin"))

"""
TC = O(N/2)
SC = O(N/2)
"""