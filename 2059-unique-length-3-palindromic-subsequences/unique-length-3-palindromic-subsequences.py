class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for c in set(s):
            i = s.find(c)
            j = s.rfind(c)
            if i != -1 and j != -1 and i != j:
                ans += len(set(s[i+1:j]))
        return ans
