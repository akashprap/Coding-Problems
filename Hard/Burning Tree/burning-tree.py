#User function Template for python3
from collections import deque,defaultdict
class Solution:
    def mark_parent(self,root,parent,start):
        q=deque()
        q.append(root)
        target=None
        while q:
            node=q.popleft()
            if node.data==start:
                target=node
            if node.left:
                q.append(node.left)
                parent[node.left]=node
            if node.right:
                q.append(node.right)
                parent[node.right]=node
        return target
    def minTime(self, root,start):
        # code here
        parent_mark=defaultdict(int)
        target=self.mark_parent(root,parent_mark,start)
        visited=defaultdict(bool)
        q=deque()
        q.append(target)
        visited[target]=True
        time=0
        while q:
            size=len(q)
            f=0
            for i in range(size):
                node=q.popleft()
                if node.left and visited[node.left]==False:
                    f=1
                    q.append(node.left)
                    visited[node.left]=True
                if node.right and visited[node.right]==False:
                    f=1
                    q.append(node.right)
                    visited[node.right]=True
                if parent_mark[node]and visited[parent_mark[node]]==False:
                    f=1
                    q.append(parent_mark[node])
                    visited[parent_mark[node]]=True
            if f:
                time+=1
        return time



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

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

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends