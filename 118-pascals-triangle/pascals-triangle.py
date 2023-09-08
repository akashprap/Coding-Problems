class Solution:
    # def comb(self,n,r):
    #     return math.factorial(n)//(math.factorial(n-r)*(math.factorial(r)))
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        for i in range(1,numRows):
            temp=1
            zu=[1]
            for j in range(i):
                temp=temp*(i-j)
                temp=temp//(j+1)
                zu.append(temp)
            ans.append(zu)
        return ans

