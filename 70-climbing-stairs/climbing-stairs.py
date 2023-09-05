class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def f(ind):
            if ind==n:
                return 1
            if ind>n:
                return 0
            return f(ind+1)+f(ind+2)
        return f(0)
        