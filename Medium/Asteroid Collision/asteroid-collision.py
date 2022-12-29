#User function Template for python3

class Solution:
    def asteroidCollision(self, N, ast):
        # Code here
        st=[]
        for i in ast:
            if i>0:
                st.append(i)
            else:
                while st and st[-1]>0 and st[-1]<abs(i):
                    st.pop()
                if st and st[-1]==abs(i):
                    st.pop()
                elif st  and st[-1]>abs(i):
                    continue
                else:
                    st.append(i)
            
        return st
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        asteroids = list(map(int, input().split()))
        ob = Solution()
        res = ob.asteroidCollision(N, asteroids)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends