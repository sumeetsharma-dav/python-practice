class Solution:
    def insetion_sort(self,nums):
        for i in range (1,len(nums)):
            key = nums[i]
            j = i - 1
            while key < nums[j] and j >= 0:
                nums[j+1] = nums[j]
                j -=1
            nums[j+1] = key
        return nums
def main():
    s = Solution()
    nums = [3,5,6,4,8,9,10,7,1]
    result = s.insetion_sort(nums)
    print(result)
if __name__ == "__main__":
    main()