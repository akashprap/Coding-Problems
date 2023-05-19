

from typing import List
from collections import defaultdict
class Solution:
    def kthSmallestNum(self, n: int, ranges: List[List[int]], q: int, queries: List[int]) -> List[int]:
        ranges.sort(key=lambda x: x[0])
        ans = []
        rng = []
        num_ranges = len(ranges)
        cur = ranges[0]
        
        for i in range(1, num_ranges):
            if ranges[i][0] <= cur[1]:
                cur[1] = max(ranges[i][1], cur[1])
            else:
                rng.append(cur)
                cur = ranges[i]
        rng.append(cur)
        
        num_merged_ranges = len(rng)
        
        for i in range(q):
            qu = queries[i]
            
            for j in range(num_merged_ranges):
                tot = rng[j][1] - rng[j][0] + 1
                if tot >= qu:
                    ans.append(rng[j][0] + qu - 1)
                qu -= tot
                if qu <= 0:
                    break
            if qu > 0:
                ans.append(-1)
        
        return ans

        
        
        
            
            
        



#{ 
 # Driver Code Starts


class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        ranges=IntMatrix().Input(n, 2)
        
        
        q = int(input())
        
        
        queries=IntArray().Input(q)
        
        obj = Solution()
        res = obj.kthSmallestNum(n, ranges, q, queries)
        
        IntArray().Print(res)
        

# } Driver Code Ends