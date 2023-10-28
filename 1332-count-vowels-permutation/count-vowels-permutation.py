class Solution:
    def countVowelPermutation(self, n: int) -> int:
        #if a-->e then i am storing like e--->a
        # dct={
        #     "a":{"e","i","u"},
        #     "e":{"a","i"},
        #     "i":{"e","o"},
        #     "o":{"i"},
        #     "u":{"i","o"}
        # }

        a,e,i,o,u=1,1,1,1,1
        for _ in range(n-1):
            a,e,i,o,u=e+i+u,a+i,e+o,i,i+o
        return (a+e+o+i+u)%(10**9+7)
