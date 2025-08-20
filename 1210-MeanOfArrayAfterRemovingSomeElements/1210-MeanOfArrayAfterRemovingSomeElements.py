# Last updated: 8/20/2025, 5:52:24 AM
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        
        p = int((5/100) * len(arr))

        arr = arr[p:-p:]
        
        return sum(arr)/len(arr)        