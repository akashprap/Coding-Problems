class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        limit=len(arr)//4
        c=Counter(arr)
        for i in c:
            if c[i]>limit:
                return i
                