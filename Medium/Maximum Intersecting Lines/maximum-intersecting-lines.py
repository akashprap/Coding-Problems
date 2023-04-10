#User function Template for python3
from collections import defaultdict
class Solution: 
    def maxIntersections(self, lines, N):
        d=defaultdict(int)
        # print(lines)
        for s,e in lines:
            d[s]+=1
            d[e+1]-=1
        # print(d)
        maxi=1
        cusum=0
        for  node in sorted(d):
            cusum+=d[node]
            maxi=max(maxi,cusum)
        return maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N = int(input())
        lines=[[] for j in range(N)]
        for j in range(2):
            prr = [int(i) for i in input().split()] 
            for i in range(N): 
                lines[i].append(prr[i])
            
    
        ob = Solution()
        print(ob.maxIntersections(lines, N))
        
        T -= 1

# } Driver Code Ends