class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count, cache = 0, {}
        def dfs(node):
            nonlocal count
            if not node:
                return 0, 0
            if node in cache:
                return cache[node]
            sumLeft, cntLeft = dfs(node.left)
            sumRight, cntRight = dfs(node.right)
            sumAll, cntAll = sumLeft + sumRight + node.val, cntLeft + cntRight + 1
            if sumAll // cntAll == node.val:
                count += 1
            cache[node] = sumAll, cntAll
            return sumAll, cntAll

        dfs(root)
        return count
