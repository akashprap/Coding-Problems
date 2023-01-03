#User function Template for python3
import bisect
class Solution:
    def removeStudents(self, h,n):
        temp=[]
        
        temp.append(h[0])
        for i in range(1,n):
            if h[i]>temp[-1]:
                temp.append(h[i])
                
            else:
                idx=bisect.bisect_left(temp,h[i])
                temp[idx]=h[i]
        #print(temp)
        return n-len(temp)
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        H=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.removeStudents(H,N))
# } Driver Code Ends