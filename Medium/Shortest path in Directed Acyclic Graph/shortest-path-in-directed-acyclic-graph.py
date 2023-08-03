#User function Template for python3
from typing import List
from collections import defaultdict
class Solution:
    def dfs(self,i,vis,adj,st):
        vis[i]=1
        for node in adj[i]:
            if vis[node[0]]==0:
                self.dfs(node[0],vis,adj,st)
        st.append(i)
        # return st
        
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        for a,b,w in edges:
            adj[a].append([b,w])
        st=[]
        vis=[0]*n
        for i in range(n):
            if not vis[i]:
                self.dfs(i,vis,adj,st)
        dist=[float('inf') for i in range(n)]
        dist[0]=0
        while st:
            node=st.pop()
            for neigh in adj[node]:
                if dist[neigh[0]]>dist[node]+neigh[1]:
                    dist[neigh[0]]=dist[node]+neigh[1]
        for i in range(n):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist
        



#{ 
 # Driver Code Starts

#Initial Template for Python 3

from typing import List




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
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends