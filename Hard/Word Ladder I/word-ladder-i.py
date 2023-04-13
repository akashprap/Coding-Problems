class Solution:
	def wordLadderLength(self, bw, ew, wordList):
		#Code here
		wl = set(wordList)
        q = deque()
        q.append((bw, 1))
        if bw in wl:
            wl.remove(bw)
        while q:
            word, steps = q.popleft()
            if word == ew:
                return steps
            l = len(word)
            for i in range(l):
                for j in range(97, 123):
                    c = chr(j)
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wl:
                        wl.remove(new_word)
                        q.append((new_word, steps+1))
        return 0
#{ 
 # Driver Code Starts
from collections import deque 
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
		ans = obj.wordLadderLength(startWord, targetWord, wordList)
		print(ans)

# } Driver Code Ends