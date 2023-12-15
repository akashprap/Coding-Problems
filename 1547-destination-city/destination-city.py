class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start=set()
        for a,b in paths:
            start.add(a)
        for a,b in paths:
            if b in start:
                continue
            else:
                return b


        