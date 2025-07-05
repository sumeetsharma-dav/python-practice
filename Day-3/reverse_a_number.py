class Solution:
    def reverseANumber(self,num):
        n = abs(num)
        res = 0
        if n == 0:
            return n
        while n > 0:
            res = res * 10 + n%10
            n = n // 10
        return res if num > 0 else res * -1

def main():
    s = Solution()
    number = 12345
    result = s.reverseANumber(number)
    print(f"the reverse of number {number} is {result}")

if __name__ == "__main__":
    main()

"""
Time complexity O(log10(n))
Space complexity O(1)
"""