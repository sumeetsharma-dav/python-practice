class Solution:
    def spiral(self,nums):
        top = 0
        left = 0
        result = []
        right = len(nums[0]) - 1
        bottom = len(nums) - 1
        print(right, bottom)
        while left <=right and top <= bottom:
            print(left, right, top, bottom)
            for i in range (left,right + 1):
                result.append(nums[top][i])
            top += 1
            for i in range (top, bottom+1):
                result.append(nums[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right,left-1, -1):
                    result.append(nums[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range (bottom, top-1,-1):
                    result.append(nums[i][left])
                left +=1
        return result
def main():
    s = Solution()
    nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(s.spiral(nums))
if __name__ == "__main__":
    main()