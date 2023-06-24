#User function Template for python3

class Solution:
    def klengthpref(self,arr,n,k,s):
        # return list of words(str) found in the board  
        ans=0
        if len(s)<k:
            return 0
        for i in arr:
            if i[:k]==s[:k]:
                ans+=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr = []
        for x in range(n):
            s1 = input()
            arr.append(s1)
        k = int(input())
        s = input()
        obj = Solution()
        print(obj.klengthpref(arr,n,k,s))
        
        
# } Driver Code Ends