class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        res = {}
        for c in s:
            if c not in res:
                res[c] = 1
            else:
                res[c] += 1
                if res[c] >= 2:
                    res[c] -= 2
                    length += 2
        if 1 in res.values():
            length += 1
        return length
            
