class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i]==goal[0]:
                if goal==s[i:]+s[:i]:
                    return True
                else:
                    continue
        return False