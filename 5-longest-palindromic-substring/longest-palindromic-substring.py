class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return 0
        max_length = 1
        start = 0
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            if i < len(s) - 1 and s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_length = 2
        for length in range(3, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    start = i
                    max_length = length
        return s[start:start + max_length]
