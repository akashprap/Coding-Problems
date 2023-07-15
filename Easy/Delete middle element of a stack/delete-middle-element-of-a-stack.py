#User function Template for python3
import math
class Solution:
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        
        if sizeOfStack == 0:
            return

        mid = sizeOfStack // 2

        def deleteMiddle(stack, current):

            if current == mid:
                stack.pop()
                return

            top = stack.pop()
            deleteMiddle(stack, current + 1)

            stack.append(top)

        deleteMiddle(s, 0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
sys.setrecursionlimit(10**8)

def main():
    t=int(input())
    while(t>0):
        sizeOfStack=int(input())
        myStack=[int(x) for x in input().strip().split()]
        ob = Solution()
        ob.deleteMid(myStack,sizeOfStack)
        while(len(myStack)>0):
            print(myStack[-1],end=" ")
            myStack.pop()
        print()
        t-=1


if __name__=="__main__":
    main()
    
    
# } Driver Code Ends