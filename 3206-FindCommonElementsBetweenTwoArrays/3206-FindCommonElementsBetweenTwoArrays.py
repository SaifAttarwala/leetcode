# Last updated: 8/24/2025, 11:54:55 PM
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res1 = res2 = 0

        for x in range(len(nums1)):
            if nums1[x] in nums2:
                res1 += 1
        for x in range(len(nums2)):
            if nums2[x] in nums1:
                res2 += 1
        
        return [res1,res2]