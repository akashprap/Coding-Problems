class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dct=defaultdict(int)
        for i in arr:
            dct[i%k]+=1
        for i in dct:
            
            if i==0:
                if dct[i]%2!=0:
                    return False
            elif dct[i]!=dct[abs(k-i)]:
                return False
            elif k%2==0 and i==k//2:
                if dct[i]%2!=0:
                    return False
            # print(i,dct[i])
        return True
