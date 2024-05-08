class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans={}
        temp = score.copy()
        score.sort(reverse = True)
        for i in range(1,len(score)+1):
            if i==1:
                ans[score[i-1]]="Gold Medal"
            elif i==2:
                ans[score[i-1]] = "Silver Medal"
            elif i==3:
                ans[score[i-1]] = "Bronze Medal"
            else:
                ans[score[i-1]] = str(i)
        res=[]
        for i in temp:
            res.append(ans[i])
        return res