class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            dct = defaultdict(int)
            for j in range(i, n):
                dct[s[j]] += 1
                if len(dct) > 1: 
                    maxi = max(dct.values())
                    mini = min(dct.values())
                    ans += maxi - mini
        return ans
