class Solution:
    def getRow(self, r: int) -> List[int]:
        if r==0:
            return [1]
        elif r==1:
            return [1,1]
        arr=[1,1]
        for i in range(2,r+1):
            temp=[arr[0]]
            for k in range(len(arr)-1):
                temp.append(arr[k]+arr[k+1])
            temp.append(1)
            arr=temp
        return arr



        