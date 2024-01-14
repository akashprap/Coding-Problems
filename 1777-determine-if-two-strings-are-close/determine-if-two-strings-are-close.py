class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w_dct1=Counter(word1)
        w_dct2=Counter(word2)
        return (set(word1)==set(word2)) and (sorted([i for _,i in w_dct1.items()])==sorted([i for _,i in w_dct2.items()]))