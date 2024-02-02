class Solution:
    def isvalid(self,num):
        n=len(str(num))
        if n==1:
            return True
        else:
            num=str(num)
            for i in range(1,n):
                if int(num[i])-int(num[i-1])!=1:
                    return False
            return True
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        st='123456789'
        i=0
        ans=[]
        for i in range(9):
            for j in range(i+1,9):
                num=int(st[i:j+1])
                if num>=low and num<=high:
                    if self.isvalid(num):
                        ans.append(num)
                elif num<low:
                    continue
                else:
                    break
                # else:
                #     while st[i:j+1] and (int(st[i:j+1])<low or int(st[i:j+1])>high):
                #         i+=1
                #     if num>=low and num<=high:
                #         ans.append(num)
        return sorted(ans)
            
