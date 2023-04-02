from collections import deque
class Solution:
    # def check(self,start,adj,vis,pathvis):
    #     vis[start]=1
    #     pathvis[start]=1
    #     for  node in adj[start]:
    #         if vis[node]==0:
    #             if self.check(node,adj,vis,pathvis)==True:
    #                 return True
    #         elif pathvis[node]==1:
    #             return True
    #     pathvis[start]=0
    #     return False
    def isCyclic(self, V, adj):
        # vis=[0]*V
        # pathvis=[0]*V
        # for i in range(V):
        #     if vis[i]==0:
        #         if self.check(i,adj,vis,pathvis)==True:
        #             return True
        # return False
        
        
        #using kahn's bfs algorithm
        
        indegree=[0]*V
        for i in range(V):
            for node in adj[i]:
                indegree[node]+=1
        q=deque()
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        topo=0
        while q:
            node=q.popleft()
            topo+=1
            for neighbor in adj[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)
        # print(topo)
        if topo!=V:
            return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

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
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends