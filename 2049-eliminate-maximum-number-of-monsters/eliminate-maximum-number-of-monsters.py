class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time=[(i/j) for i,j in zip(dist,speed)]
        time.sort()
        c=1
        p=0
        ans=1
        time=time[1:]
        while time:
            if time[0]>c:
                time.pop(0)
                c+=1
                ans+=1
            else:
                return ans
        return ans
                

