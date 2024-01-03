class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        temp=[]
        for i in bank:
            tt=(i.count('1'))
            if tt:
                temp.append(tt)
        ans=0
        for i in range(1,len(temp)):
            ans+=temp[i-1]*temp[i]
        return ans
