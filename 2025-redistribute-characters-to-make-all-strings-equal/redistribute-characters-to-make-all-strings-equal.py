class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dct=defaultdict(int)
        n=len(words) 
        if n==1:
            return True
        for i in words:
            for j in i:
                dct[j]+=1
        print(n,dct)
        prev=0
        for i in dct:
            if not prev:
                if dct[i]%n==0:
                    prev=dct[i]
                else:
                    return False
            else:
                if dct[i]%n!=0:
                    return False
        return True
