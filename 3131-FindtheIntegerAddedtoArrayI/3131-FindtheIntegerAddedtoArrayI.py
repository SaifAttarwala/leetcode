# Last updated: 7/27/2025, 5:26:00 AM
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        return -(nums1[0]-nums2[0])
        