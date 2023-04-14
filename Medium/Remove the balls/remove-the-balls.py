from typing import List


class Solution:
    def finLength(self, N : int, color : List[int], radius : List[int]) -> int:
        # code here
        st=[]
        i=0
        while i<N:
            # print(st)
            if not st:
                st.append((color[i],radius[i]))
                # i+=1
            elif st and color[i]==st[-1][0] and radius[i]==st[-1][1]:
                st.pop()
                # continue
                # i+=1
            else:
                st.append((color[i],radius[i]))
            i+=1
        return len(st)
        



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
        
        
        color=IntArray().Input(N)
        
        
        radius=IntArray().Input(N)
        
        obj = Solution()
        res = obj.finLength(N, color, radius)
        
        print(res)
        

# } Driver Code Ends