# Last updated: 8/24/2025, 1:29:58 AM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        return median(nums1)
        