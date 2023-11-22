class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d=defaultdict(list)
        for rowi,r in enumerate(mat):
            for coli,c in enumerate(mat[rowi]):
                d[rowi+coli].append(c)
        ans=[]
        for i in sorted(d.keys()):
            if i&1:
                ans+=d[i]
            else:
                ans+=reversed(d[i])
        return ans