class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time=sorted([(i/j) for i,j in zip(dist,speed)])
        n,ans,i=len(time),1,1
        while i<n:
            if time and time[i]>ans: ans+=1;i+=1
            else: return ans
        return ans