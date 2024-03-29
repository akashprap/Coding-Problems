#User function Template for python3

##Complete this code

class Solution:
    def arrange(self, arr, n):
        # Modify the array elements to store both the original value and the new value.
        for i in range(n):
            arr[i] += (arr[arr[i]] % n) * n
        
        # Retrieve the new values from modified elements.
        for i in range(n):
            arr[i] //= n


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.arrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends