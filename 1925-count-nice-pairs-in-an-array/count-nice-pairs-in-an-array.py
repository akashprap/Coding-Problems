from collections import Counter
class Solution:
    def countNicePairs(self, nums):
        res = 0
        tt = []
        for i in nums:
            n=i
            tpm = n%10
            n//=10
            while n>0:
                tpm=tpm*10+(n%10)
                n//=10
            tt.append(i - tpm)
        # print(tt)
        c = Counter(tt)
        for i in c:
            if c[i]>1:
                res+=(c[i]*(c[i]-1))//2
        return res%(10**9+7)