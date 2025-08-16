# Last updated: 8/16/2025, 7:34:04 AM
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res1 = []
        res2 = []

        for x in nums1:
            if x not in nums2:
                res1.append(x)
        for x in nums2:
            if x not in nums1:
                res2.append(x)
        
        return list(set(res1)), list(set(res2))