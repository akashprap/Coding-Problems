#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    def maxDifferenceBST(self,root, target):
        #code here
        def dfs(node, path_sum, target):
            if not node:
                return None, float('-inf')

            path_sum += node.data
            if node.data == target:
                return node, path_sum

            if node.data > target:
                return dfs(node.left, path_sum, target)
            else:
                return dfs(node.right, path_sum, target)

        def leaf_sum(node, curr_sum):
            if not node:
                return float('inf')

            if not node.left and not node.right:
                return curr_sum + node.data

            return min(leaf_sum(node.left, curr_sum + node.data), leaf_sum(node.right, curr_sum + node.data))

        target_node, target_sum = dfs(root, 0, target)

        if not target_node:
            return -1

        return target_sum - leaf_sum(target_node, 0)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def createNode(self, data):
        return Node(data)
    
    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left, data)
            else:
                node.right = self.insert(node.right, data)
            return node

    def traverseInorder(self, root):
        if root is not None:
            print(root.data, end= " ")
            self.traverseInorder(root.left)
            self.traverseInorder(root.right)
    
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr = input().strip().split()
        root = None
        tree = Tree()
        root = tree.insert(root, int(arr[0]))
        for j in range(1, n):
            root = tree.insert(root, int(arr[j]))
        #tree.traverseInorder(root)
        target = int(input())
        
        res = Solution().maxDifferenceBST(root, target)
        print(res)

# } Driver Code Ends