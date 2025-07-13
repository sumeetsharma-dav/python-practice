class Solution:
    def max_profit(self,nums):
        minn = float("+inf")
        profit = 0
        for i in nums:
            minn = min(minn,i)
            profit = max(profit,i-minn)
        return profit
def main():
    s = Solution()
    nums = [7,2,1,5,6,4,8]
    print(s.max_profit(nums))

if __name__ == "__main__":
    main()