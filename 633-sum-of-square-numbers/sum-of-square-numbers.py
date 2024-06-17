class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(c**0.5)
        while a <= b:
            cur = a*a + b*b
            if cur == c:
                return True
            elif cur < c:
                a += 1
            else:
                b -= 1
        return False
