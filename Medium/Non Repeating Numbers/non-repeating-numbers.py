#User function Template for python3

class Solution:
    def singleNumber(self, nums):
        xorr = 0
        for num in nums:
            xorr ^= num
        
        # Find the rightmost set bit in the XOR result
        rightmost_set_bit = 1
        while (rightmost_set_bit & xorr) == 0:
            rightmost_set_bit <<= 1
        
        # Divide the numbers into two groups based on the rightmost set bit
        x1, x2 = 0, 0
        for num in nums:
            if (num & rightmost_set_bit) == 0:
                x1 ^= num
            else:
                x2 ^= num
        
        # Return the numbers in increasing order
        return min(x1, x2), max(x1, x2)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends