class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d =defaultdict(list)
        ans = []
        for word in strs:
            # print(sorted(word))
            sorted_word = ''.join(sorted(word))
            d[sorted_word].append(word)
        for key in d:
            ans.append(d[key])
        return ans