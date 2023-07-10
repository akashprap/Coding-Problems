#User function Template for python3

class Solution:
    def transpose(self, matrix, n):
        # Write Your code here
        for i in range(n):
            for j in range(i+1):
                temp=matrix[j][i]
                matrix[j][i]=matrix[i][j]
                matrix[i][j]=temp
        


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    matrix = [
            list(map(int,input().split()))
            for _ in range(n)
        ]
        
    ob = Solution()
    ob.transpose(matrix, n)
    
    for row in matrix:
        print(*row)
    
# } Driver Code Ends