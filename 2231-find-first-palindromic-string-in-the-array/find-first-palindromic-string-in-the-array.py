class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        ans=""
        for i in words:
            if i==i[::-1]:
                return i
        return ans