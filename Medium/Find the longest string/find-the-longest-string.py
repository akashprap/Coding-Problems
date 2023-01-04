#User function Template for python3


class Solution():
    def longestString(self, arr, n):
        #your code goes here
        arr.sort(key=lambda x: (len(x), x))
        ans = ""
        m = {""}
        for e in arr:
            if e[:-1] in m:
                m.add(e)
                ans = max(ans, e, key=len)
                
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [i for i in input().split()]
        print(Solution().longestString(arr,n))
# } Driver Code Ends