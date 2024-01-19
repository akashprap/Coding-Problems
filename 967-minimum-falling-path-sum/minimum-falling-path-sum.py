class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        for col in range(cols):
            dp[0][col] = matrix[0][col]
        for row in range(1, rows):
            for col in range(cols):
                dp[row][col] = matrix[row][col] + min(
                    dp[row - 1][max(0, col - 1)],
                    dp[row - 1][col],
                    dp[row - 1][min(cols - 1, col + 1)]
                )
        return min(dp[-1])