class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxi=0
        prevx=points[0][0]
        for x,_ in points[1:]:
            maxi=max(maxi,x-prevx)
            prevx=x
        return maxi
