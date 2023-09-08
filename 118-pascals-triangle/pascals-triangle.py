class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans=[[1]]
        for i in range(1,n):
            temp=[1]
            for j in range(1,i):
                temp.append(ans[-1][j-1]+ans[-1][j])
            temp.append(1)
            # print(ans)
            ans.append(temp)
        return ans


        