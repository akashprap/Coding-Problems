#User function Template for python3

class Solution():
    def solve(self, a, b, c):
        #your code goes here
        maxNum = max(a,b,c)
        if(maxNum<=(2*(a+b+c-maxNum+1))):
            return a+b+c
        else:
            return -1
# abcabc
# aabaabaacaac

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import Counter
for _ in range(int(input())):
    a, b, c=map(int,input().split())
    obj = Solution()
    res = obj.solve(a, b, c)
    
    print(res)
# } Driver Code Ends