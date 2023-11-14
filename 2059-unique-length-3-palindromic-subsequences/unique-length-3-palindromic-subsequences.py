class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        char_positions = {c: [s.find(c), s.rfind(c)] for c in set(s)}
        for positions in char_positions.values():
            if positions[0] != positions[1]:
                ans += len(set(s[positions[0]+1:positions[1]]))
        return ans
