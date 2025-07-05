class Solution:
    def armstrong_number(self,num):
        n = abs(num)
        p = len(str(abs(num)))
        sum = 0
        while n > 0:
            sum = sum + pow(n%10,p)
            n = n // 10
        return sum == abs(num)

def main():
    s = Solution()
    number = -1634
    result = s.armstrong_number(number)
    print(f"{number} is armstrong {result}")

if __name__ == "__main__":
    main()

"""
Time complexity O(log10(n))
Space complexity O(1)
"""