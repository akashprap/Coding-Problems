#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
from collections import Counter,defaultdict
class Solution:
    def isStraightHand(self, N, gs, hand):
        # Code here
        if N%gs!=0:
            return False
        mp=Counter(hand)
        hand.sort()
        for card in hand:
            if not mp[card]:
                continue
            for j in range(gs):
                cur=card+j
                if cur not in mp:
                    return False
                mp[cur]-=1
        return True
        
        # 1 2 2 3 3 4 6 7 8
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, groupSize = list(map(int, input().split()))
        hand = list(map(int, input().split()))
        ob = Solution()
        res = ob.isStraightHand(N, groupSize, hand);
        print(res)
# } Driver Code Ends