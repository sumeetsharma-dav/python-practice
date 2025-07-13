class Solution:
    def merge_sorted_no_dup(self,nums1,nums2):
        i = 0
        j = 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                if len(result) == 0 or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i += 1
            else:
                if len(result) == 0 or result[-1] != nums2[j]:
                    result.append(nums2[j])
                j += 1
        if i < len(nums1):
            while i < len(nums1):
                if len(result) == 0 or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i += 1
        if j < len(nums2):
            while j < len(nums2):
                if len(result) == 0 or result[-1] != nums2[j]:
                    result.append(nums2[j])
                j += 1
        return result
def main():
    s = Solution()
    nums1 = [1,1,1,1,2,4,6,7]
    nums2 = [1,2,3,6,7,8,9,10]
    print(s.merge_sorted_no_dup(nums1, nums2))
if __name__ == "__main__":
    main()


"""
TC: O(N) as looping thought longest list one time
SC: O(1)
"""