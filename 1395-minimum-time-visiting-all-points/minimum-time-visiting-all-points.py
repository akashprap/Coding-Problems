class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans=0
        prea,preb=points[0]
        for a,b in points[1:]:
            ans+=max(abs(a-prea),abs(b-preb))
            prea,preb=a,b
        return ans