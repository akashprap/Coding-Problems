class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        ans1=0
        ans2=0
        for i in range(n):
            # 01010101
            if i%2==0:
                if s[i]=="0":
                    continue
                else:
                    ans1+=1
            else:
                if s[i]=="1":
                    continue
                else:
                    ans1+=1
        # for i in range(n):
        #     # 10101010
        #     if i%2!=0:
        #         if s[i]=="0":
        #             continue
        #         else:
        #             ans2+=1
        #     else:
        #         if s[i]=="1":
        #             continue
        #         else:
        #             ans2+=1
        return min(ans1,n-ans1)
