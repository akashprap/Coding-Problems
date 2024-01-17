class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=defaultdict(int)
        s=set()
        for i in arr:
            d[i]+=1
        for i in d:
            s.add(d[i])
        if len(s)==len(d):
            return True
        return False
        