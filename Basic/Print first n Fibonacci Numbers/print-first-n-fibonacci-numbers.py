#User function Template for python3

class Solution:
    # first n fibonacci numbers.
    def printFibb(self,n):
        list_num = []
        for i in range(n):
            if i==0 or i==1:
                list_num.append(1)
            else:
                list_num.append(list_num[i-1]+list_num[i-2])
        return list_num


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends