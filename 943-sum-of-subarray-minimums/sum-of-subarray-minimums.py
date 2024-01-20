class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        prev = [0]*len(arr)
        for i in range(len(arr)):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)
        next_ = [0]*len(arr)
        stack = []
        for i in range(len(arr)-1, -1, -1):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            next_[i] = stack[-1] if stack else len(arr)
            stack.append(i)
        return sum((i - prev[i]) * (next_[i] - i) * arr[i] for i in range(len(arr))) % MOD
