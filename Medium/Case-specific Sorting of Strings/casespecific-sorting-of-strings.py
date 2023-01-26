#User function Template for python3

class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        #code here
        cap=[]
        sma=[]
        for i in s:
            if i<="z" and i>="a":
                sma.append(i)
            else:
                cap.append(i)
        cap.sort(key=lambda x: ord(x))
        sma.sort(key=lambda x:ord(x))
        i,j=0,0
        ans=""
        for ind in range(n):
            if s[ind] <="z" and s[ind]>="a":
                ans+=sma[i]
                i+=1
            else:
                ans+=cap[j]
                j+=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))
# } Driver Code Ends