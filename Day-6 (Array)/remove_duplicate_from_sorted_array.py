class Solution:
    def rem_dup_sorted_arr(self,nums):
        i = 0
        j = i + 1
        while i <= j and j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        return i + 1
def main():
    s = Solution()
    nums = [1,1,1,1,2,2,2,3,4,4,7,9,9,10]
    print(s.rem_dup_sorted_arr(nums))
if __name__ == "__main__":
    main()

"""
TC: O(N)
SC: O(1)
"""