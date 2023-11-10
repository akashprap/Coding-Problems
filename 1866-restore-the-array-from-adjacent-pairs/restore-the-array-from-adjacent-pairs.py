from collections import defaultdict, Counter
from typing import List

class Solution:
    def restoreArray(self, ap: List[List[int]]) -> List[int]:
        dct = defaultdict(list)
        l = [j for i in ap for j in i]
        st = [e for e, cnt in Counter(l).items() if cnt == 1]
        
        for a, b in ap:
            dct[a].append(b)
            dct[b].append(a)

        ans = []
        if len(st) == 1:
            ans.append(st[0])
        else:
            ans.append(st[0] if st[0] in dct[st[1]] else st[1])

        sss = set(ans)
        while len(ans) < len(ap) + 1:
            for adj in dct[ans[-1]]:
                if adj not in sss:
                    ans.append(adj)
                    sss.add(adj)

        return ans
