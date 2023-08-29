class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        currow=0
        curcol=col-1
        while currow>=0 and currow<row and curcol>=0 and curcol<col:
            if target==matrix[currow][curcol]:
                return True
            elif target>matrix[currow][curcol]:
                currow+=1
            else:
                curcol-=1
        return False