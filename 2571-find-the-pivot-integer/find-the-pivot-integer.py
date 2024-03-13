class Solution:
    def pivotInteger(self, n: int) -> int:
        ss = (n*(n+1))//2
        curr_sum = 0
        for i in range(1,n+1):
            curr_sum += i
            if ss-curr_sum+i == curr_sum :
                return i
        return -1