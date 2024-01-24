# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,s):
        if root==None:
            return 0
        if root.val in s:
            s.remove(root.val)
        else:
            s.add(root.val)
        #print(s)
        if root.left==None and  root.right==None:
            if len(s)<=1:
                return 1
            else:
                return 0
        left=self.dfs(root.left,set(s))
        right=self.dfs(root.right,set(s))
        return left+right
        
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        s=set()
        return self.dfs(root,s)