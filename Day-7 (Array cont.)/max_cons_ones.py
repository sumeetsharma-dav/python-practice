class Solution:
    def mac_cons_ones(self,nums):
        maxi = 0
        current = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                current += 1
            else:
                maxi = max(maxi, current)
                current = 0
            i += 1
        return max(maxi, current)
def main():
    s = Solution()
    nums = [1,0,1,1,1,1,0,0,0,1,1,1,1,1,1,1]
    print(s.mac_cons_ones(nums))
if __name__ == "__main__":
    main()

"""
TC: O(N)
SC: O(1)
"""