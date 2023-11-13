class Solution:
    def sortVowels(self, s: str) -> str:
        vow=['a','e','i','o','u']
        vowel=[]
        cons=[]
        for i in s:
            if i.lower() in vow:
                vowel.append(i)
            else:
                cons.append(i)
        temp=[]
        vowel.sort(key=lambda x:ord(x))
        po=0
        poc=0
        for i in s:
            if i.lower() in vow:
                temp.append(vowel[po])
                po+=1
            else:
                temp.append(cons[poc])
                poc+=1
        return "".join(temp)
            
            
            
        