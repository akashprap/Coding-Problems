# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mapparent(self,root,parentmap):
        q=deque([root])
        while q:
            for i in range(len(q)):
                curr=q.popleft()
                
                if curr.left:
                    q.append(curr.left)
                    parentmap[curr.left]=curr

                if curr.right:
                    q.append(curr.right)
                    parentmap[curr.right]=curr
        return parentmap
    def findnode(self,node,root):
        if root:
            if root.val==node:
                return root
            left=self.findnode(node,root.left)
            if left:
                return left
            right=self.findnode(node,root.right)
            if right:
                return right
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        dct=defaultdict()
        parentmap=self.mapparent(root,dct)
        parentmap[root]=-1
        startnode=self.findnode(start,root)
        t=0
        qu=deque([startnode])
        vis=set()
        vis.add(startnode)
        while qu:
            f=0
            for i in range(len(qu)):
                curr=qu.popleft()
                if curr.left:
                    if curr.left not in vis:
                        f=1
                        qu.append(curr.left)
                        vis.add(curr.left)
                if curr.right:
                    if curr.right not in vis:
                        f=1
                        vis.add(curr.right)
                        qu.append(curr.right)
                if parentmap[curr]!=-1:
                    if parentmap[curr] not in vis:
                        f=1
                        vis.add(parentmap[curr])
                        qu.append(parentmap[curr])
            if f:
                t+=1
        return t


        