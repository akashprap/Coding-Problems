# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def inor(root):
            nonlocal ans
            if root:
                inor(root.left)
                ans.append(root.val)
                inor(root.right)
        inor(root)
        return ans
        