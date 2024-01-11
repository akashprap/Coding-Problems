class Solution:
    def __init__(self):
        self.ans=0
    def solve(self,root,minn,maxx,ans):
        if not root:
            return
        self.ans=max(self.ans,abs(minn-root.val),abs(maxx-root.val))
        minn=min(root.val,minn)
        maxx=max(root.val,maxx)
        self.solve(root.left,minn,maxx,self.ans)
        self.solve(root.right,minn,maxx,self.ans)
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.solve(root,root.val,root.val,self.ans)
        return self.ans
        