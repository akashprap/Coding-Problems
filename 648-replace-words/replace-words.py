class Solution:
    def replaceWords(self, dic: List[str], sentence: str) -> str:
        ans=[]
        for i in sentence.split(" "):
            minLength = -1
            minstr = ""
            for j in dic:
                if i.startswith(j):
                    if minLength ==-1:
                        minLength = len(j)
                        minstr = j
                    else:
                        if len(j)<minLength:
                            minLength = len(j)
                            minstr = j
                else:
                    continue
            else:
                if minLength == -1:
                    ans.append(i)
                else:
                    ans.append(minstr)
                # print(ans)
        return " ".join(ans)