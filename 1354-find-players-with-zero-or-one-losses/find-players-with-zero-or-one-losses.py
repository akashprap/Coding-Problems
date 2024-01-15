class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        looser_count=defaultdict(int)
        players=set()
        for w,l in matches:
            players.add(w)
            players.add(l)
            looser_count[l]+=1
        winner=[]
        looser=[]
        for i in players:
            if i in looser_count:
                if looser_count[i]==1:
                    looser.append(i)
            else:
                winner.append(i)
        return [sorted(winner),sorted(looser)]

        
        