"""
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
1<=n[i]<=10
n can have any number of elements
m can have any number of elements
Print the frequecnt of elements of m in n
"""
class Solution:
    def print_freq(self,n,m):
        o = [0] * 11
        for i in n:
            o[i] = o[i] + 1
        for i in m:
            if i > 10 or i <= 0:
                print(f"{i} occurs {0} times in n")
            else:
                print(f"{i} occurs {o[i]} times in n")
    def print_freq_map(self,n,m):
        d = {}
        for i in n:
            d[i] = d.get(i,0) + 1
        for i in m:
                print(f"{i} occurs {d.get(i,0)} times in n")
def main():
    s = Solution()
    n = [5,3,2,2,1,5,5,7,5,10]
    m = [10,111,1,9,5,67,2]
    s.print_freq_map(n,m)

if __name__ == "__main__":
    main()

"""
TC = O(n+m)
SC = O(11)
"""
