class Solution:
    def isPathCrossing(self, path: str) -> bool:
        ss=set()
        x,y=0,0
        ss.add((x,y))
        for p in path:
            if p=="N":
                y+=1
            elif p=="E":
                x+=1
            elif p=="S":
                y-=1
            else:
                x-=1
            # print((x,y),ss)
            if (x,y) in ss:
                return True
            else:
                ss.add((x,y))
        return False