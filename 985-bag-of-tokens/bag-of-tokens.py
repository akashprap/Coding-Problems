class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens) - 1
        cur_score = mx_score = 0
        while l <= r:
            if tokens[l] <= power:
                power -= tokens[l]
                cur_score += 1
                mx_score = max(mx_score, cur_score)
                l += 1
            elif cur_score >= 1:
                power += tokens[r]
                cur_score -= 1
                r-=1
            else:
                break
        return mx_score