#User function Template for python3

def reverseWord(s):
    #your code here
    s=[i for i in s]
    def reverse(i,j,s):
        if i>j:
            return
        s[i],s[j]=s[j],s[i]
        reverse(i+1,j-1,s)
    reverse(0,len(s)-1,s)
    return("".join(s))
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends