class Solution:
    def two_sum(self,nums,k):
        dict = {}
        for i in range (0,len(nums)):
            complement = k - nums[i]
            if complement in dict:
                return [dict[complement],i]
            dict[nums[i]] = i
        return [-1,-1]
def main():
    s = Solution()
    nums = [5,9,1,2,4,15,6,3]
    k = 13
    print(s.two_sum(nums,k))
if __name__ == "__main__":
    main()
"""
TC: O(N)
SC: O(N)
"""