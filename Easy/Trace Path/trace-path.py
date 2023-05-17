#User function Template for python3

class Solution:
    def isPossible(self, n, m, s):
        # code here
        minx,maxx,miny,maxy=0,0,0,0
        x,y=0,0
        for i in range(len(s)):
            if s[i]=="L":
                y-=1
            elif s[i]=="R":
                y+=1
            elif s[i]=="D":
                x+=1
            else:
                x-=1
            minx=min(minx,y)
            miny=min(miny,x)
            maxx=max(maxx,y)
            maxy=max(maxy,x)
        return int((maxx-minx)<m and (maxy-miny)<n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        s = input()
        
        ob = Solution()
        print(ob.isPossible(n, m, s))
# } Driver Code Ends