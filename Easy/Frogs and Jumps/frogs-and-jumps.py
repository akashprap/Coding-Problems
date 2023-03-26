#User function Template for python3
from typing import List
class Solution:
    def unvisitedLeaves(self, N: int, leaves: int, frogs: List[int]) -> int:
        visited = [False] * (leaves + 1)

        for i in range(N):
            jump = frogs[i]
            if jump <= leaves and not visited[jump]:
                for k in range(jump, leaves+1, jump):
                    visited[k] = True

        cnt = 0
        for i in range(1, leaves+1):
            if not visited[i]:
                cnt += 1

        return cnt



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N, leaves = [int(i) for i in input().split()]
        frogs = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.unvisitedLeaves(N, leaves, frogs))
        
        T -= 1
# } Driver Code Ends