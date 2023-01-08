#User function Template for python3

class Solution:
    def countPairs (self, n, arr, k):
        # code here
        cnt = 0;
 
    # making every element of arr in
    # range 0 to k - 1
        for i in range(n):
            arr[i] = (arr[i] + k) % k;
     
        # create an array hash
        hash = [0]*k;
     
        # store to count of element of arr
        # in hash
        for i in range(n):
            hash[arr[i]] += 1;
     
        # count the pair whose absolute
        # difference is divisible by k
        for i in range(k):
            cnt += (hash[i] * (hash[i] - 1)) / 2;
     
        # print value of count
        return(int(cnt));

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        k=int(input())
        
        ob = Solution()
        print(ob.countPairs(n,arr,k))
# } Driver Code Ends