#User function Template for python3

class Solution:
    def secondSmallest(self, S, D):
        # code hereif
        su=0
        for i in range(D):
            su+=9
        if S>=su:
            return "-1"
        num=[1]*D
        for i in range(D-1,0,-1):
            d=min(S-1,9)
            num[i]=d
            S-=d
        if S>9:
            return "-1"
        num[0]=S
        # print(num)
        for i in range(D-1,0,-1):
            if num[i]!=0 and num[i-1]!=9:
                num[i]-=1
                num[i-1]+=1
                st=""
                for j in range(D):
                    st+=str(num[j])
                return st
            # return -1
    
        return -1       
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S,D=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.secondSmallest(S,D))
# } Driver Code Ends