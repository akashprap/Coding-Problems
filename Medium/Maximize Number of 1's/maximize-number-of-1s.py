#User function Template for python3


# m is maximum of number zeroes allowed 
# to flip, n is size of array 
def findZeroes(arr, n, m) :
    # code here
    i=0
    j=0
    count=0
    maxi=0
    for j in range(n):
        if arr[j]==0:
            count+=1
        # j+=1
        while count>m:
            if arr[i]==0:
                count-=1
            i+=1
        maxi=max(maxi,j-i+1)
        # j+=1
    return maxi

#{ 
 # Driver Code Starts
#Initial Template for Python 3




# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int , input().strip().split()))
        m=int(input())
        ans= findZeroes(arr, n, m)
        print(ans)
        tc=tc-1
# } Driver Code Ends