class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dct=defaultdict(int)
        for i in arr:
            dct[i]+=1
        temp=[]
        for key,v in dct.items():
            temp.append((key,v))
        temp.sort(key=lambda x:x[1])
        leng=len(temp)
        i=0
        while k!=0:
            # print(k,temp[i][1])
            if temp[i][1]<=k:
                print(temp[i][1])
                k-=temp[i][1]
                leng-=1
                i+=1
            else:
                return leng
        return leng
            
