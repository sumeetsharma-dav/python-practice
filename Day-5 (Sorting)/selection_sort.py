"""
Simple sorting algorithm that repeatedly compares adjacent elements and swaps them if they are in the wrong order.
"""
class Solution:
    def selectionSort(self,nums):
        for current_pointer in range (0,len(nums)):
            for next_pointer in range (current_pointer + 1 , len(nums)):
                if nums[current_pointer] > nums[next_pointer]:
                    nums[current_pointer], nums[next_pointer] = nums[next_pointer], nums[current_pointer]
        return nums

def main():
    s = Solution()
    nums = [5,7,8,4,1,6,9,2]
    result = s.selectionSort(nums)
    print(result)
if __name__ == "__main__":
    main()

"""
TC: O(N(N+1)/2)
SC: O(1)
"""