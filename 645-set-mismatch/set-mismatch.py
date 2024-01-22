class Solution:
    def findErrorNums(self, A):
        N = len(A)
        count1 = [0] * (N+1)
        for x in A:
          count1[x] += 1
        for x in range(1, len(A)+1):
            if count1[x] == 2:
                twice = x
            if count1[x] == 0:
                never = x
        return twice, never