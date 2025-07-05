class Solution:
    def countDigits(self, num):
        n = num
        count = 0
        if n == 0:
            return 1
        while n > 0:
          n = n//10
          count = count + 1
        return count

def main():
    s = Solution()
    n = 0
    result = s.countDigits(n)
    print(f"number for digits in {n} is {result}")

if __name__ == "__main__":
    main()

"""
Time complexity O(log10(n))
Space complexity O(1)
"""