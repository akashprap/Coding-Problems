from typing import List
class Solution:
    def solve(self, N : int, A : List[int], B : List[int]) -> int:
        ea, eb, oa, ob = [],[],[],[]
        for i in range(N):
            if A[i]%2 == 0:
                ea.append(A[i])
            else:
                oa.append(A[i])
            
            if B[i]%2 == 0:
                eb.append(B[i])
            else:
                ob.append(B[i])
                
        if len(oa) != len(ob) or len(ea) != len(eb):
            return -1
        
        for e in [oa, ob, ea, eb]:
            e.sort()
            
        a = oa+ea
        b = ob+eb
        
        v, cnt = 0, 0
        for i in range(len(a)):
            d = a[i]-b[i]
            if d > 0:
                cnt += d//2
            v += d
        
        if v != 0:
            return -1
        return cnt



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
        
        
        A=IntArray().Input(N)
        
        
        B=IntArray().Input(N)
        
        obj = Solution()
        res = obj.solve(N, A, B)
        
        print(res)
        

# } Driver Code Ends