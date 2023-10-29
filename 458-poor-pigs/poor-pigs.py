class Solution:
    def f(self,mid,buckets,it):
        return (it+1)**mid>=buckets

    def poorPigs(self, buckets: int, mdie: int, mtest: int) -> int:
        if buckets==1:
            return 0
        it=mtest//mdie
        l=1
        r=buckets
        ans=0
        while l<=r:
            mid=(l+r)//2
            if self.f(mid,buckets,it):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans