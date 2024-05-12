class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ss=set(banned)
        currsum = 0
        curr = 1
        length = 0
        while currsum<=maxSum and curr<=n:
            if curr not in ss:
                currsum+=curr
                if currsum>maxSum:
                    return length
                else:
                    curr+=1
                    length +=1
            elif currsum>maxSum:
                break
            else:
                curr+=1
        return length
        