"""
1. print x n times
   print 15 4 times
2. print 1 to n

"""
class Solution:
    def recursion_simple(self,x,n):
        if n == 0:
            return
        print(x)
        self.recursion_simple(x,n-1)
    def printToN(self,i,n):
        if i > n:
            return
        self.printToN(i+1,n)
        print(i)
    def print1ToNTail(self,n):
        if n == 0:
            return
        self.print1ToNTail(n-1)
        print(n)
    def print1ToNHead(self,n):
        if n == 0:
            return
        print(n)
        self.print1ToNHead(n-1)

def main():
    s = Solution()
    x = 15
    n = 4
    #s.recursion_simple(x,n)
    s.print1ToNHead(5)
    s.print1ToNTail(5)

if __name__ == "__main__":
    main()
"""
TC = O(N+1)
SC = O(N+1)
"""