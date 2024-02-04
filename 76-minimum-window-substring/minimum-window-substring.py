from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        s_count = defaultdict(int)
        ans = ""
        min_len = float('inf')
        i = 0
        count = 0

        for j in range(len(s)):
            s_count[s[j]] += 1

            if s_count[s[j]] <= t_count[s[j]]:
                count += 1

            while count == len(t):
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    ans = s[i:j+1]

                if s_count[s[i]] == t_count[s[i]]:
                    count -= 1

                s_count[s[i]] -= 1
                i += 1

        return ans
