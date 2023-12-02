class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans=0
        # c1=Counter()
        c2=Counter(chars)
        for i in words:
            if Counter(i)<=c2:
                ans+=len(i)
            
        return ans
        