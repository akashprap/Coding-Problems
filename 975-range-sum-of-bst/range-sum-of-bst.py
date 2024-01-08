# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inor(root):
            if root:
                inor(root.left)
                arr.append(root.val)
                inor(root.right)
        arr=[]
        inor(root)
        ind1=bisect.bisect_left(arr,low)
        ind2=bisect.bisect_left(arr,high)
        # print(arr,ind1,ind2)
        return sum(arr[ind1:ind2+1])