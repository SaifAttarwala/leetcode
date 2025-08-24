# Last updated: 8/24/2025, 11:55:13 PM
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr = Counter(arr)
        if len(arr.values()) == len(set(arr.values())):
            return True
        else:
            return False
        