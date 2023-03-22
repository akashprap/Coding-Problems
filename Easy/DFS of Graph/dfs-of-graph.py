#User function Template for python3

class Solution:
    def dfs(self,start,adj,vis,ans):
        vis[start]=1
        ans.append(start)
        for node in adj[start]:
            if not vis[node]:
                vis[node]=1
                self.dfs(node,adj,vis,ans)
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        visited=[0]*(V+1)
        ans=[]
        self.dfs(0,adj,visited,ans)
        return ans


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends