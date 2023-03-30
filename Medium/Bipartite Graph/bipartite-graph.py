from collections import deque
class Solution:
    def bfs(self,node,adj,color):
        q=deque()
        q.append(node)
        color[node]=0
        while q:
            po=q.popleft()
            for neighbor in adj[po]:
                if color[neighbor]==-1:
                    color[neighbor]=1-color[po]
                    q.append(neighbor)
                elif color[neighbor]==color[po]:
                    return False
        return True
            
	def isBipartite(self, V, adj):
		#code here
		color=[-1]*V
		for i in range(V):
		    if color[i]==-1:
		        if self.bfs(i,adj,color)==False:
		            return False
	    return True


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends