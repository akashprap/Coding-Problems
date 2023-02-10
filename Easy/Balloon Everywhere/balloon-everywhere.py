from collections import defaultdict
class Solution:
    def maxInstance(self, s : str) -> int:
        # code here
        d=defaultdict(int)
        for i in s:
            d[i]+=1
        return min(d['b'],d['a'],d['n'],d['l']//2,d['o']//2)

#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        s = (input())
        
        obj = Solution()
        res = obj.maxInstance(s)
        
        print(res)

# } Driver Code Ends