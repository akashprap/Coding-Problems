class Solution:
    def dfs(self,sr,sc,image,color,prev_c):
        n=len(image)
        m=len(image[0])
        image[sr][sc]=color
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        for i in range(4):
            nr=sr+dr[i]
            nc=sc+dc[i]
            if nr>=0 and nr<n and nc>=0 and nc<m and image[nr][nc]==prev_c:
                image[nr][nc]=color
                self.dfs(nr,nc,image,color,prev_c)
	def floodFill(self, image, sr, sc, color):
		#Code here
		if image[sr][sc]==color:
            return image
        prev_c=image[sr][sc]
        self.dfs(sr,sc,image,color,prev_c)
        return image



#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		image = []
		for _ in range(n):
			image.append(list(map(int, input().split())))
		sr, sc, newColor = input().split()
		sr = int(sr); sc = int(sc); newColor = int(newColor);
		obj = Solution()
		ans = obj.floodFill(image, sr, sc, newColor)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
# } Driver Code Ends