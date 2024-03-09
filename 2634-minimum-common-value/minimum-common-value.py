class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s1=set(nums1)
        s2=set(nums2)
        s=s1.intersection(s2)
        if len(s)==0:
            return -1
        else:
            mini=1e9+1
            for i in s:
                if i<=mini:
                    mini=min(mini,i)
            return mini
        