class Solution:
    def f(self, ind, arr, dp, temp):
        if ind == len(arr):
            return len(temp)
        if (ind, temp) in dp:
            return dp[(ind, temp)]

        nottake = self.f(ind + 1, arr, dp, temp)
        curr = arr[ind]
        take = 0
        if len(set(curr + temp)) == len(curr + temp):
            take = self.f(ind + 1, arr, dp, temp + arr[ind])

        dp[(ind, temp)] = max(take, nottake)
        return dp[(ind, temp)]

    def maxLength(self, arr: List[str]) -> int:
        dp = {}
        temp = ""
        return self.f(0, arr, dp, temp)
