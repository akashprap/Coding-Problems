#User function Template for python3

from typing import List
from collections import deque

class Solution:
    def findSequences(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        st = set(wordList)
        q = deque()
        q.append([beginWord])
        usedOnLevel = [beginWord]
        level = 0
        ans = []
        while q:
            vec = q.popleft()
            if len(vec) > level:
                level += 1
                for it in usedOnLevel:
                    st.discard(it)
                usedOnLevel = []

            word = vec[-1]
            if word == endWord:
                if len(ans) == 0:
                    ans.append(vec)
                elif len(ans[0]) == len(vec):
                    ans.append(vec)
            for i in range(len(word)):
                original = word[i]
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    word = word[:i] + c + word[i+1:]
                    if word in st:
                        vec.append(word)
                        q.append(vec[:])
                        usedOnLevel.append(word)
                        vec.pop()
                word = word[:i] + original + word[i+1:]
        return ans


#{ 
 # Driver Code Starts
from collections import deque 
import functools

def comp(a, b):
    x = ""
    y = ""
    for i in a:
        x += i 
    for i in b:
        y += i
    if x>y:
        return 1
    elif y>x:
        return -1 
    else:
        return 0

if __name__ == '__main__':
    T=int(input())
    for tt in range(T):
        n = int(input())
        wordList = []
        for i in range(n):
            wordList.append(input().strip())
        startWord = input().strip()
        targetWord = input().strip()
        obj = Solution()
        ans = obj.findSequences(startWord, targetWord, wordList)
        if len(ans)==0:
            print(-1)
        else:
            ans = sorted(ans, key=functools.cmp_to_key(comp))
            for i in range(len(ans)):
                for j in range(len(ans[i])):
                    print(ans[i][j],end=" ")
                print()

# } Driver Code Ends