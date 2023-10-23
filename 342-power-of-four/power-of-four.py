class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        val=math.log(abs(n),4)
        return ceil(val)==floor(val)