class Solution:
    def max_sum(self,nums):
        max_sum = float("-inf")
        total = 0
        for i in nums:
            total = i + total
            max_sum = max(max_sum,total)
            if total < 0:
                total = 0
        return max_sum
def main():
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.max_sum(nums))
if __name__ == "__main__":
    main()

"""
SC: O(1)
TC: O(N)
"""