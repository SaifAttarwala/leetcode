# Last updated: 8/16/2025, 5:50:13 AM
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        expected_heights = sorted(heights)

        for i in range(len(heights)):
            if heights[i] != expected_heights[i]:
                res += 1
        return res