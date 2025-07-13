class Solution:
    def find_largest(self, nums):
        largest = nums[0]
        for n in nums:
            largest = max(largest,n)
        return largest
def main():
    s = Solution()
    nums = [55,32,-97,99,3,67]
    print(s.find_largest(nums))
if __name__ == "__main__":
    main()


"""
TC: O(N)
SC: O(1)
"""