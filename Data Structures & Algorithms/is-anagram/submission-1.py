class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charsCountS, charsCountT = {}, {}

        for chS in s:
            if chS not in charsCountS:
                charsCountS[chS] = 1
            else:
                charsCountS[chS] += 1
        
        for chT in t:
            if chT not in charsCountT:
                charsCountT[chT] = 1
            else:
                charsCountT[chT] += 1

        return charsCountS == charsCountT