class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x:abs(x))
        return list(map(lambda x: x**2,nums))