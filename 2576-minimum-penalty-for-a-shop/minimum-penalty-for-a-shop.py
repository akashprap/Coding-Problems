class Solution:
    def bestClosingTime(self, cust: str) -> int:
        n = len(cust)
        no_cust = [0] * n
        cust_come = [0] * n
        for i in range(n):
            if cust[i] == 'N':
                no_cust[i] = 1
            else:
                cust_come[i] = 1
        for i in range(1, n):
            no_cust[i] += no_cust[i - 1]
            cust_come[n - i - 1] += cust_come[n - i]
        ans = float("inf")
        closing_time = 0
        for i in range(n + 1):
            penalty = 0
            if i > 0:
                penalty += no_cust[i - 1]
            if i < n:
                penalty += cust_come[i]
            if penalty < ans:
                ans = penalty
                closing_time = i
        return closing_time
