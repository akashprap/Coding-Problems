#User function Template for python3
from collections import defaultdict,deque
class Solution:
    def isPossible(self,V,prerequisites):
        #code here
        adj=defaultdict(list)
        for a,b in prerequisites:
            adj[a].append(b)
            
        #topo sort to detect cycle
        
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
        if topo==V:
            return True
        return False
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends