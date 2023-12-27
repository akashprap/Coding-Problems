class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev=colors[0]
        ans=0
        maxi=neededTime[0]
        for i in range(1,len(colors)):
            if colors[i]==prev:
                if neededTime[i]>maxi:
                    ans+=maxi
                    maxi=neededTime[i]
                else:
                    ans+=neededTime[i]
            else:
                prev=colors[i]
                curval=neededTime[i]
                maxi=curval
        return ans
