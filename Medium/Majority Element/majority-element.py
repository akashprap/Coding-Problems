#User function template for Python 3
import math
from collections import Counter
class Solution:
    def majorityElement(self, nums, n):
        cnt=0
        for i in range(n):
            if cnt==0:
                cnt+=1
                el=nums[i]
            elif nums[i]==el:
                cnt+=1
            else:
                cnt-=1
        cn1=0
        for i in range(n):
            if nums[i]==el:
                cn1+=1
        if cn1>n//2:
            return el
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends