#User function Template for python3
from collections import deque,defaultdict
from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, ad: List[List[int]]) -> List[int]:
        # # code here
        q=deque()
        q.append(0)
        ans=[]
        vis=[0]*V
        while q:
            l=len(q)
            for i in range(l):
                node=q.popleft()
                if not vis[node]:
                    ans.append(node)
                    vis[node]=1
                    for nei in adj[node]:
                        q.append(nei)
        return ans


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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends