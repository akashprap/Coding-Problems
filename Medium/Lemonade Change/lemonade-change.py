#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def lemonadeChange(self, N, bills):
        # Code here
        d={}
        d[5]=0
        d[10]=0
        d[20]=0
        for i in range(N):
            if(bills[i]==5):
                d[5]+=1
            elif(bills[i]==10):
                if(d[5]==0):
                    return False
                d[10]+=1
                d[5]-=1
            else:
                if(d[10]!=0 and d[5]!=0):
                    d[20]+=1
                    d[10]-=1
                    d[5]-=1
                elif(d[10]==0 and d[5]>=3):
                    d[5]-=3
                else:
                    return False
        return True



#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        bills = list(map(int, input().split()))
        ob = Solution()
        res = ob.lemonadeChange(N, bills)
        print(res)
# } Driver Code Ends