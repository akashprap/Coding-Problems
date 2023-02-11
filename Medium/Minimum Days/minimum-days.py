from typing import List


class Solution:
    def getMinimumDays(self, N : int, S : str, P : List[int]) -> int:
        # code here
        cons=0
        for i in range(len(S)-1):
            if(S[i]==S[i+1]):
                cons+=1
        S=list(S)
        if cons==0:
            return 0
        for i in range(N):
            index=P[i]
            if(index !=0 and S[index]==S[index-1]):
                cons-=1
            if(index!=N-1 and S[index]==S[index+1]):
                cons-=1
            if(cons==0):
                return i+1
            S[index]='?'
        return -1


#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        S = (input())
        
        
        P=IntArray().Input(N)
        
        obj = Solution()
        res = obj.getMinimumDays(N, S, P)
        
        print(res)
        

# } Driver Code Ends