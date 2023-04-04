#User function Template for python3
from collections import deque,defaultdict
class Solution:
    def findOrder(self,dict, N, K):
        adj=defaultdict(list)
        
        for i in range(N-1):
            s1=dict[i]
            s2=dict[i+1]
            for j in range(min(len(s1),len(s2))):
                if s1[j]!=s2[j]:
                    adj[ord(s1[j])-97].append(ord(s2[j])-97)
                    break
        
        
        indegree=[0]*K
        for i in range(K):
            for nodes in adj[i]:
                indegree[nodes]+=1
        q=deque()
        for i in range(K):
            if indegree[i]==0:
                q.append(i)
        ans=[]
        while q:
            node=q.popleft()
            ans.append(node)
            for n in adj[node]:
                indegree[n]-=1
                if indegree[n]==0:
                    q.append(n)
        st=""
        for i in ans:
            st+=chr(i+97)
        # print(st)
        return st
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends