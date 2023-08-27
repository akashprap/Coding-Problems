class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        memo = {}
        
        def jump(curr, k):
            if (curr, k) in memo:
                return memo[(curr, k)]
            
            if curr == stones[-1]:
                return True
            
            for pos_jump in [k + 1, k, k - 1]:
                if pos_jump > 0 and curr + pos_jump in stone_set:
                    if jump(curr + pos_jump, pos_jump):
                        memo[(curr, k)] = True
                        return True
            
            memo[(curr, k)] = False
            return False
        
        return jump(0, 0)
