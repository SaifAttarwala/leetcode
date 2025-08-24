# Last updated: 8/24/2025, 11:55:18 PM
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        trust_scores = [0 for x in range(n+1)]
        print(trust_scores)
        for person1, person2 in trust:
            trust_scores[person1] -= 1
            trust_scores[person2] += 1
        print(trust_scores)
        
        for x in range(1,n+1):
            if trust_scores[x] == n-1:
                return x
        return -1

        