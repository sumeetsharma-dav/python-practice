class Solution:
    def bubble_sort(self, nums):
        max = len(nums)
        is_swaped = False
        for k in range (len(nums) - 2, -1, -1):
            for i in range (0,k+1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    is_swaped = True
            if is_swaped == False:
                break
        return nums
def main():
    s = Solution()
    #nums = [5,8,1,6,9,2,4]
    #nums = [9,8,7,6,5,4,3,2,1]
    nums = [1,2,3,4,5,6,7,8,9,10]
    result = s.bubble_sort(nums)
    print(result)
if __name__ == "__main__":
    main()

"""
TC: O(N^2)
SC: O(1)
"""