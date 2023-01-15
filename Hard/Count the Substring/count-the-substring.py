#User function Template for python3


from collections import defaultdict
class Solution():
    def countSubstring(self, S):
        acc, le, carry = 0, defaultdict(lambda:0), defaultdict(lambda:0)
        le[0] = 1; carry[1] = 1
        ans = 0
        for c in S:
            v = 1 if c=='1' else -1
            acc += v
            le[acc] += 1 + carry[acc]
            carry[acc+1] += 1 + carry[acc]
            carry[acc] = 0
            ans += le[acc-1]
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        print(Solution().countSubstring(s))
# } Driver Code Ends