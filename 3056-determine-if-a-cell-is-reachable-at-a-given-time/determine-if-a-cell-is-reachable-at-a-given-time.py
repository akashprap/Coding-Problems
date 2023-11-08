class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        min_steps = max(abs(fx - sx), abs(fy - sy))
        if t < min_steps:
            return False
        else:
            if sx==fx and sy==fy:
                if t!=1:
                    return True
                else:
                    return False
            else:
                return True