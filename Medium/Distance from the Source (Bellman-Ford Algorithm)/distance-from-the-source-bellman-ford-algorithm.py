#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        m=10**8
        dist=[m]*V
        dist[S]=0
        for i in range(V-1):
            for u,v,wt in edges:
                if dist[u]!=m and dist[v]>dist[u]+wt:
                    dist[v]=dist[u]+wt
        #Nth iteration
        for u,v,wt in edges:
            if dist[v]!=m and dist[v]>dist[u]+wt:
                return [-1]
        return dist
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends