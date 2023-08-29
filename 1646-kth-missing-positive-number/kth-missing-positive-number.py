class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l=0
        h=len(arr)-1
        while l<=h:
            mid=(l+h)//2
            missing=arr[mid]-(mid+1)
            if missing<k:
                l=mid+1
            else:
                h=mid-1
        return h+1+k
