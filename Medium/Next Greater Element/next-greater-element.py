#User function Template for python3


class Solution:

    def nextLargerElement(self,arr,n):

        stack=[arr[-1]]

        

        maximum=arr[-1]

        

        arr[-1]=-1

        for i in range(-2,-n-1,-1):

            if arr[i]>=maximum:

                maximum=arr[i]

                stack.append(arr[i])

                arr[i]=-1

            else:

                while stack!=[]:

                    if stack[-1]>arr[i]:

                        value=arr[i]

                        arr[i]=stack[-1]

                        stack.append(value)

                        break

                    else:

                        stack.pop()
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends