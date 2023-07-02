#User function Template for python3

class Solution:
    def setSetBit(self, x, y, l, r):
        # code here
        mask = (1<<(r - l + 1))
        mask-=1 
        mask = (mask <<(l - 1))
        mask = mask & y
        x = x | mask
        return x
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        x = int(arr[0])
        y = int(arr[1])
        l = int(arr[2])
        r = int(arr[3])
        
        ob = Solution()
        print(ob.setSetBit(x, y, l, r))
# } Driver Code Ends