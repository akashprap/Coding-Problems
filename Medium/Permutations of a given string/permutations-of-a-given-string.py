#User function Template for python3

class Solution:
    def permute(self,s,res,mp,temp,zz):
        if len(temp)==len(s):
            if "".join(temp) not in zz:
                res.append("".join(temp))
                zz.add("".join(temp))
                return
        for i in range(len(s)):
            if i not in mp:
                mp.add(i)
                temp.append(s[i])
                self.permute(s,res,mp,temp,zz)
                temp.pop()
                mp.remove(i)
        return res
                
            
    def find_permutation(self, S):
        # Code here
        s=[i for i in S]
        s.sort()
        return self.permute(s,[],set(),[],set())



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends