#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, x): 
    #Your code here
        l=1
        h=x//2
        ans=1
        while l<=h:
            mid=(l+h)//2
            if mid**2==x:
                ans=mid
                break
            elif mid**2>x:
                h=mid-1
            else:
                ans=mid
                l=mid+1
        return ans
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends