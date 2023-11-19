class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        c = Counter(nums)
        keys = sorted(c.keys(), reverse=True)
        ans, total = 0, 0
        for i in range(len(keys) - 1):
            total += c[keys[i]]
            ans += total
        return ans
