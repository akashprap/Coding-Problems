class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        maxi=0
        n=len(s)
        for ind in range(len(s)):
            #expand as s[i] as centre of string
            #this will produce only odd length substring
            i=ind
            j=ind
            while i>=0 and j<n:
                if s[i]==s[j]:
                    if (j-i+1)>maxi:
                        maxi=j-i+1
                        ans=s[i:j+1]
                    i-=1
                    j+=1
                else:
                    break
            #to generate even length
            i=ind
            j=ind+1
            while i>=0 and j<n:
                if s[i]==s[j]:
                    if (j-i+1)>maxi:
                        maxi=j-i+1
                        ans=s[i:j+1]
                    i-=1
                    j+=1
                else:
                    break
        return ans


        