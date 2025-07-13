class Solution:
    def long_cons_seq(self,nums):
        my_set = set()
        longest = 0
        for i in nums:
            my_set.add(i)
        for i in range (0,len(nums)):
            count = 1
            num = nums[i]
            if nums[i] - 1 in my_set:
                continue
            while num+1 in my_set:
                count += 1
                num = num + 1
            longest = max(count,longest)
        return longest


def main():
    s = Solution()
    #nums = [1,99,108,98,2,5,3,100,1,1,101,102]
    nums = [1]
    print(s.long_cons_seq(nums))

if __name__ == "__main__":
    main()


"""
TC: O(N) + O(N) + O(N)
SC: O(N)
"""