# Last updated: 7/22/2025, 1:05:36 AM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while 0 in nums1[m:]:
            nums1.remove(0)
            
        nums1.extend(nums2)
        nums1.sort()

        
        
        