#User function Template for python3

from collections import deque
from typing import List

class Solution:
    def numberOfEnclaves(self, board: List[List[int]]) -> int:
        n = len(board)
        m = len(board[0])
        visited = set()
        queue = deque()
        ans = 0

        # Check the first and last rows
        for i in range(n):
            if board[i][0] == 1:
                queue.append((i, 0))
                visited.add((i, 0))
            if board[i][m - 1] == 1:
                queue.append((i, m - 1))
                visited.add((i, m - 1))

        # Check the first and last columns
        for j in range(m):
            if board[0][j] == 1:
                queue.append((0, j))
                visited.add((0, j))
            if board[n - 1][j] == 1:
                queue.append((n - 1, j))
                visited.add((n - 1, j))

        # BFS traversal
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= n or nc < 0 or nc >= m or board[nr][nc] == 0 or (nr, nc) in visited:
                    continue
                queue.append((nr, nc))
                visited.add((nr, nc))

        # Count the remaining unvisited cells
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1 and (i, j) not in visited:
                    ans += 1

        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends