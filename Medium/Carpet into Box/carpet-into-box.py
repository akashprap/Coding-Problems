#User function Template for python3


class Solution:
    def sove(self,a,b,c,d):
        ans=0
        while a>c:
            ans+=1
            a=a//2
        while b>d:
            ans+=1
            b=b//2
        return ans
    def carpetBox(self, A,B,C,D):
        #code here
        return min(self.sove(A,B,C,D),self.sove(B,A,C,D))



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
        T=int(input())
        while(T>0):
            A,B,C,D = map(int, input().split())
            
            obj = Solution()
            print(obj.carpetBox(A,B,C,D))
            
            T-=1


if __name__ == "__main__":
    main()


# } Driver Code Ends