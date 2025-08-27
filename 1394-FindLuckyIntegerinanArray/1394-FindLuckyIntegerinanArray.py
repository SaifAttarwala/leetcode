# Last updated: 8/27/2025, 10:13:14 PM
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        lucky = -1
        
        for num, count in freq.items():
            if num == count:
                lucky = max(lucky,num)
        
        return lucky