#User function Template for python3
from collections import defaultdict
class Solution:
    def dfs(self,i,adj,vis,st):
        vis[i]=1
        for it in adj[i]:
            if not vis[it]:
                self.dfs(it,adj,vis,st)
        st.append(i)
        
        
    def dfs2(self,i,vis,adjT):
        vis[i]=1
        for it in adjT[i]:
            if not vis[it]:
                self.dfs2(it,vis,adjT)
                
                
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        vis=[0]*V
        st=[]
        for i in range(V):
            if not vis[i]:
                self.dfs(i,adj,vis,st)
        
        adjT=defaultdict(list)
        for i in range(V):
            for it in adj[i]:
                adjT[it].append(i)
            
                
        vis=[0]*V
        scc=0
        while st:
            node=st.pop()
            if vis[node]==0:
                scc+=1
                self.dfs2(node,vis,adjT)
        return scc
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends