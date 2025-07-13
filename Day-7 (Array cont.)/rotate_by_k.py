class Solution:
    def rotate_by_k(self,nums,k):
        r = k%len(nums)
        self.rotate(nums,0,len(nums)-r-1)
        self.rotate(nums,len(nums)-r, len(nums)-1)
        self.rotate(nums,0,len(nums)-1)
        return nums
    def rotate(self,nums,l,r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums
def main():
    s = Solution()
    nums = [5,2,3,9,0,6,10,7]
    print(s.rotate_by_k(nums,5))
if __name__ == "__main__":
    main()

"""
SC: O(1)
TC: O(K + N-K) = O(N)
"""