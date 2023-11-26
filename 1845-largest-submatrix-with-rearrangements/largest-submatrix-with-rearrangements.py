from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        # Preprocess the matrix
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        
        max_area = 0
        for i in range(m):
            # Sort each row
            row = sorted(matrix[i], reverse=True)
            for j in range(n):
                # Calculate maximum area
                max_area = max(max_area, row[j]*(j+1))
        
        return max_area
