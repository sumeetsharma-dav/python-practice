class Solution:
    def set_zeroes(self,nums):
        copy_nums = nums
        rows = len(nums)
        cols = len(nums[0])
        row_track = [0] * rows
        col_track = [0] * cols
        print(row_track,col_track)
        for i in range (0,rows):
            for j in range (0,cols):
                if nums[i][j] == 0:
                    row_track[i] = -1
                    col_track[j] = -1
        for i in range (0,rows):
            for j in range (0,cols):
                if row_track[i] == -1 or col_track[j] == -1:
                    nums[i][j] = 0
        return nums

def main():
    s = Solution()
    nums = [[7,9,2,3],[20,8,0,10],[29,0,-10,5],[4,14,6,7]]
    print(s.set_zeroes(nums))

if __name__ == "__main__":
    main()

"""
TC: O(2(N*M)
SC: O(N + M)
"""