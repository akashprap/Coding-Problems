class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time=sorted([(i/j) for i,j in zip(dist,speed)])
        n=len(time)
        c=1
        ans=1
        i=1
        while i<n:
            if time and time[i]>c:
                c+=1
                ans+=1
                i+=1
            else: return ans
        return ans
                

