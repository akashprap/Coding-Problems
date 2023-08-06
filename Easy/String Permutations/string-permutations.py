#User function Template for python3

class Solution:
    def f(self,ind,l,s,mapp,res,temp):
        if len(temp)==l:
            res.append(temp)
            return
        for i in range(0,l):
            if not mapp[i]:
                temp+=s[i]
                mapp[i]=1
                self.f(i+1,l,s,mapp,res,temp)
                mapp[i]=0
                temp=temp[:-1]
        
    def permutation(self,s):
        l=len(s)
        mapp=[0]*l
        res=[]
        self.f(0,l,s,mapp,res,"")
        res.sort()
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    while(T>0):
        s=input()
        ob=Solution()
        ans=ob.permutation(s)
        for i in ans:
            print(i,end=" ")
        print()
        
        T-=1
# } Driver Code Ends