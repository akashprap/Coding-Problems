class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def isLeaf(node):
            return node is not None and node.left is None and node.right is None

        leftLeavesSum = 0
        if isLeaf(root.left):
            leftLeavesSum += root.left.val
        else:
            leftLeavesSum += self.sumOfLeftLeaves(root.left)

        leftLeavesSum += self.sumOfLeftLeaves(root.right)

        return leftLeavesSum
