#User function Template for python3
from typing import List
from collections import deque,defaultdict
class Solution:
    def CheapestFLight(self,n,flights,src,dst,k):
        q=deque()
        adj=defaultdict(list)
        
        for s,e,w in flights:
            adj[s].append((e,w))
        dist=[1e9]*n
        dist[src]=0
        q.append((0,(src,0)))
        #(stop,(node,dist))
        while q:
            it=q.popleft()
            stop=it[0]
            node=it[1][0]
            cost=it[1][1]
            if stop>k:
                continue
            for nei in adj[node]:
                neigh=nei[0]
                edw=nei[1]
                if edw+cost<dist[neigh] and stop<=k:
                    dist[neigh]=edw+cost
                    q.append((stop+1,(neigh,dist[neigh])))
                    
            
        
        
        
        if dist[dst]==1e9:
            return -1
        return dist[dst]
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        n,edge=map(int,input().split())
        flights=[]
        for _ in range(edge):
            temp=list(map(int,input().split()))
            flights.append(temp[:])
        src=int(input())
        dst=int(input())
        k=int(input())
        obj=Solution()
        res=obj.CheapestFLight(n,flights,src,dst,k)
        print(res)

        
        
# } Driver Code Ends