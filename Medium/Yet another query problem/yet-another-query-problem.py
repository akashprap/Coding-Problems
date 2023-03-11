from typing import List

from collections import defaultdict

class Solution:
    def solveQueries(self, N : int, num : int, A : List[int], Q : List[List[int]]) -> List[int]:
        # code here
        d=defaultdict(int)
        freq=[0]*N
        for i in range(N-1,-1,-1):
            d[A[i]]+=1
            freq[i]=d[A[i]]
        vec=[]
        for l,r,k in Q:
            ans=0
            for ra in range(l,r+1):
                if freq[ra]==k:
                    ans+=1
            vec.append(ans)
        return vec



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



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        num = int(input())
        
        
        A=IntArray().Input(N)
        
        
        Q=IntMatrix().Input(num, 3)
        
        obj = Solution()
        res = obj.solveQueries(N, num, A, Q)
        
        IntArray().Print(res)
        

# } Driver Code Ends