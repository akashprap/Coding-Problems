from typing import Optional
from collections import deque
"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def findLargestSubtreeSum(self, root : Optional['Node']) -> int:
        if (root == None):    
            return 0
         
        # Variable to store maximum subtree sum.
        ans = [-999999999999]
     
        # Call to recursive function to
        # find maximum subtree sum.
        
        # code here
        def findLargestSubtreeSumUtil(root, ans):
     
    # If current node is None then
    # return 0 to parent node.
            if (root == None):
                return 0
             
            # Subtree sum rooted at current node.
            currSum = (root.data +
                       findLargestSubtreeSumUtil(root.left, ans) +
                       findLargestSubtreeSumUtil(root.right, ans))
         
            # Update answer if current subtree
            # sum is greater than answer so far.
            ans[0] = max(ans[0], currSum)
         
            # Return current subtree sum to
            # its parent node.
            return currSum
 
# Function to find largest subtree sum.
         
        # If tree does not exist,
        # then answer is 0.
        findLargestSubtreeSumUtil(root, ans)
     
        return ans[0]
        



#{ 
 # Driver Code Starts

from collections import deque
class Node:
    def __init__(self,val):
        self.data=val
        self.right=None
        self.left=None

# Function to Build Tree
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

def inputTree():
    treeString=input().strip()
    root = buildTree(treeString)
    return root
def inorder(root):
    if (root == None):
       return
    inorder(root.left);
    print(root.data,end=" ")
    inorder(root.right)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        root = inputTree();
        
        obj = Solution()
        res = obj.findLargestSubtreeSum(root)
        
        print(res)
        

# } Driver Code Ends