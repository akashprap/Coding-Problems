class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        d = set(dictionary)

        n = len(s)

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1

            for j in range(i, 0, -1):
                temp= s[j - 1:i]

                if temp in d:
                    dp[i] = min(dp[i], dp[j - 1])

        return dp[n]