class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cur=0
        ans=[]
        j=0
        for i in range(len(s)):
            if s[i]=="(":
                cur-=1
            elif s[i]==")":
                cur+=1
            if cur==0:
                ans.append(s[j:i+1])
                if i+1<len(s):
                    j=i+1
        temp=""
        for i in ans:
            temp+=i[1:-1]
        return temp


            