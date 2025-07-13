class Solution:
    def longest_seq(self,nums):
        total = 0
        maxi = 0
        for i in nums:
            num = i
            total = 1
            while num+1 in nums:
                total += 1
                num = num + 1
            maxi = max(maxi,total)
        return maxi
def main():
    s = Solution()
    nums = [1,99,108,98,2,5,3,100,1,1]
    print(s.longest_seq(nums))
if __name__ == "__main__":
    main()