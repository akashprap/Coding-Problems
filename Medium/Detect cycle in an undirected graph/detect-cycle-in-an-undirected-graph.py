from typing import List
class Solution:
    def dfs(self,start,parent,vis,adj):
        vis[start]=True
        for node in adj[start]:
            if not vis[node]:
                if self.dfs(node,start,vis,adj)==True:
                    return True
            elif node !=parent:
                return True
        return False
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		vis=[0]*V
		for i in range(V):
		    if not vis[i]:
		        if self.dfs(i,-1,vis,adj)==True:
		            return True
	    return False


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends