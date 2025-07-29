# Last updated: 7/29/2025, 5:53:34 PM
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        for i in nums1:
            if i in nums2:
                ret.append(i)
                nums2.remove(i)
        return ret
        