class Solution:
    def reverse_array(self,nums):
        l = 0
        r = len(nums) - 1
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1
        return nums
def main():
    s = Solution()
    nums = [1,2,3,4,5,6,7,8,9]
    res = s.reverse_array(nums)
    print(res)
if __name__ == "__main__":
    main()