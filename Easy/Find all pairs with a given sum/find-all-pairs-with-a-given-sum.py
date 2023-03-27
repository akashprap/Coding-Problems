from collections import defaultdict

class Solution:
    def allPairs(self, A, B, N, M, target):
        d=defaultdict(int)
        for i in range(len(B)):
            d[B[i]]=i
            
        ans=set()
        for i in range(len(A)):
            if target-A[i] in d:
                ans.add((A[i],target-A[i]))
        f=list(ans)
        f.sort(key=lambda x:x[0])
        return f

    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        N, M, X = sz[0], sz[1], sz[2]
        A = [int(x) for x in input().strip().split()]
        B = [int(x) for x in input().strip().split()]
        ob=Solution()
        answer = ob.allPairs(A, B, N, M, X)
        sz = len(answer)
        
        if sz==0 :
        	print(-1) 
        
        else: 
            
        	for i in range(sz):
        		if i==sz-1:
        		    print(*answer[i])
        		else:
        		    print(*answer[i], end=', ')
        

        T -= 1


if __name__ == "__main__":
    main()




# } Driver Code Ends