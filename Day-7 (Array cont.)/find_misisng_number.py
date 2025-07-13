class Solution:
    def find_missing(self,nums,k):
        sums = k * (k +1 ) // 2
        miss_sum = sum(nums)
        return sums - miss_sum
def main():
    s = Solution()
    nums = [0,1,2,3,4,5,7,8,9]
    k = 9
    print(s.find_missing(nums,k))
if __name__ == "__main__":
    main()

"""
TC: O(N)
SC: O(1)
"""