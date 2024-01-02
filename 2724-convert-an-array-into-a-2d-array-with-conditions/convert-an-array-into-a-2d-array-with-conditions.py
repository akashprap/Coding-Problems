class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        mat=[[]]
        for num in nums:
            for i in mat:
                if num not in i:
                    i.append(num)
                    break
            else:
                temp=[]
                temp.append(num)
                mat.append(temp)
        return mat
        