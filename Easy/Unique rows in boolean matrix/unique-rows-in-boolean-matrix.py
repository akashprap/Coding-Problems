#User function Template for python3
from collections import defaultdict
class Solution:
    def uniqueRow(self,row, col, matrix):
        dct=defaultdict(int)
        for i,j in enumerate(matrix):
            dct[tuple(j)]+=1
        ans=[]
        for rows in matrix:
            if dct[tuple(rows)]>0:
                dct[tuple(rows)]=0
                ans.append(rows)
            else:
                continue
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
    testcase = int(input())
    while(testcase):
        s = input().split()
        row = int(s[0])
        col = int(s[1])
        matrix = [[None for _ in range(col)]for _ in range(row)]
        s = input().split()
        for i in range(row):
            for j in range(col):
                matrix[i][j] = int(s[i*col+j])
        
        ob = Solution()
        a = ob.uniqueRow(row, col, matrix)
        
        for row in a:
            for value in row:
                print(value,end = " ")
            print("$",end = "")
        print()
        testcase -= 1

if __name__ == "__main__":
    main()
# } Driver Code Ends