#User function Template for python3

class Solution:
    def checkCompressed(self, S, T):
        # code here 
        i=0
        j=0
        while j<len(S) and i<len(T):
            if T[i].isdigit():
                num=0
                while i<len(T) and T[i].isdigit():
                    num=num*10+int(T[i])
                    i+=1
                j+=num
            elif T[i].isalpha():
                if T[i]!=S[j]:
                    return 0
                j+=1
                i+=1
        if j==len(S):
            return 1
        return 0
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        T = input()
        
        ob = Solution()
        print(ob.checkCompressed(S,T))
# } Driver Code Ends