#User function Template for python3


class Solution:
    def maxLength(self,arr,n):
        #code here
        ans=0
        pos=0
        neg=0
        for i in arr:
            if i==0:
                pos=0
                neg=0
            elif i>0:
                pos+=1
                if neg==0:
                    neg=0
                else:
                    neg=neg+1
            else:
                temp=pos
                if neg==0:
                    pos=0
                else:
                    pos=neg+1
                neg=temp+1
            ans=max(ans,pos)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())

            arr=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.maxLength(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends