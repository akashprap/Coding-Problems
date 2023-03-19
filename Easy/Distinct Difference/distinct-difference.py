from typing import List


class Solution:
    def getDistinctDifference(self, N : int, A : List[int]) -> List[int]:
        # code here
        setl=[0]*N
        setr=[0]*N
        set1=set()
        set2=set()
        for i in range(0,N):
            setl[i]=(len(set1))
            set1.add(A[i])
        for i in range(N-1,-1,-1):
            setr[i]=(len(set2))
            set2.add(A[i])
        ans=[0]*N
        for i in range(N):
            ans[i]=setl[i]-setr[i]
        return ans
            



#{ 
 # Driver Code Starts
# class IntArray:

#     def __init__(self) -> None:
#         pass
    
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        A=[int(i) for i in input().split()]
        
        obj = Solution()
        res = obj.getDistinctDifference(N, A)
        
        print(*res)
        

# } Driver Code Ends