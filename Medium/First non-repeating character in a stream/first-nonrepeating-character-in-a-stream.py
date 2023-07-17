#User function Template for python3

from collections import defaultdict, deque

class Solution:
    def FirstNonRepeating(self, A):
        count = defaultdict(int)
        queue = deque()

        result = []
        for char in A:
            count[char] += 1
            queue.append(char)

            while queue and count[queue[0]] > 1:
                queue.popleft()

            if queue:
                result.append(queue[0])
            else:
                result.append('#')

        return ''.join(result)


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends