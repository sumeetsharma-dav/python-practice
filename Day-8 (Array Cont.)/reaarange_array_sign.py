class Solution:
    def rearrange_opt(self, nums):
        result = [0] * len(nums)
        p = 0
        n = 1
        for i in nums:
            if i > 0:
                result[p] = i
                p += 2
            else:
                result[n] = i
                n += 2
        return result


def main():
    s = Solution()
    nums = [5, 10, -2, -1, -10, 6]
    print(s.rearrange_opt(nums))


if __name__ == "__main__":
    main()

"""
TC: O(N)
SC: O(N)
"""