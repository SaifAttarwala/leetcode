# Last updated: 8/18/2025, 3:48:18 AM
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []

        for x in range(len(arr2)):
            for y in range(len(arr1)):
                if arr1[y] == arr2[x]:
                    res.append(arr1[y])
                    arr1[y] = -1
        arr1.sort()

        for x in arr1:
            if x != -1:
                res.append(x)

        return res 