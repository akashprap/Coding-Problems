#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
from typing import List
class Node:
    def __init__(self):
        self.child = [None] * 26

def insert(s, root):
    for i in range(len(s)):
        if root.child[ord(s[i]) - ord('a')]:
            root = root.child[ord(s[i]) - ord('a')]
        else:
            root.child[ord(s[i]) - ord('a')] = Node()
            root = root.child[ord(s[i]) - ord('a')]

def find(root, s):
    for i in range(len(s)):
        if root.child[ord(s[i]) - ord('a')]:
            root = root.child[ord(s[i]) - ord('a')]
        else:
            return False
    return True

class Solution:
    def prefixSuffixString(self, s1: List[str], s2: List[str]) -> int:
        t1, t2 = Node(), Node()
        for it in s1:
            insert(it, t1)
            insert(it[::-1], t2)
        
        cnt = 0
        for it in s2:
            ok = False
            if find(t1, it) or find(t2, it[::-1]):
                cnt += 1
        return cnt




#{ 
 # Driver Code Starts.

if __name__=="__main__":
    for _ in range(int(input())):
        s1 = list(map(str, input().split()))
        s2 = list(map(str, input().split()))
        obj=Solution()
        print(obj.prefixSuffixString(s1, s2))
# } Driver Code Ends