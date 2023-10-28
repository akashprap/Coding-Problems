class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        ans = 0
        sign = -1 if s[0] == '-' else 1
        if s[0] in ['-', '+']:
            s = s[1:]
        for ch in s:
            if not ch.isdigit():
                break
            ans = ans * 10 + int(ch)
        ans *= sign
        ans = max(min(ans, 2**31 - 1), -2**31)
        return ans
