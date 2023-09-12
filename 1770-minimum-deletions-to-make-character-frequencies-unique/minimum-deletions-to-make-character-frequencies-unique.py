class Solution:
    def minDeletions(self, s: str) -> int:
        c=Counter(s)
        ss=([i for i in c.values()])
        ss.sort()
        sset=set()
        ans=0
        # print(ss,sset)
        for ind,i in enumerate(ss):
            if ind==0:
                sset.add(i)
                continue
            elif i not in sset:
                sset.add(i)
                continue
            else:
                while i in sset:
                    i-=1
                    ans+=1
                    if i==0:
                        break
                sset.add(i)
        return ans
