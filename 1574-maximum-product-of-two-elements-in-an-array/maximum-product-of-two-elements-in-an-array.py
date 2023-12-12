class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1, m2 = -1, -1
        for i in nums:
            if i >= m1:
                m1, m2 = i, m1
            elif i > m2:
                m2 = i
        return (m1-1)*(m2-1)
