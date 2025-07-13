class Solution:
    def move_zeroes(self,nums):
        max = len(nums)
        i = 0
        while i < max:
            if nums[i] == 0:
                break
            if i == max:
                return
            i += 1
        j = i + 1
        while j < max:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j +=1
        return nums

def main():
    s = Solution()
    nums = [5,2,3,9,0,6,10,7]
    print(s.move_zeroes(nums))
if __name__ == "__main__":
    main()