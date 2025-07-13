class Solution:
    def sec_largest(self,nums):
        largest = float("-inf")
        sec_largest = float("-inf")
        for n in nums:
            if n > largest:
                sec_largest = largest
                largest = n
            elif n > sec_largest and n != largest:
                sec_largest = n
        return sec_largest
def main():
    s = Solution()
    nums = [55,32,-97,99,3,67]
    print(s.sec_largest(nums))
if __name__ == "__main__":
    main()

"""
TC: O(N)
SC: O(1)
"""