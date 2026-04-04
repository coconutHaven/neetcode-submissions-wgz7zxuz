class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charsInS = {}
        for ch in s:
            if ch not in charsInS:
                charsInS[ch] = 1
            else:
                charsInS[ch] += 1
        
        charsInT = {}
        for ch in t:
            if ch not in charsInT:
                charsInT[ch] = 1
            else:
                charsInT[ch] += 1

        if charsInT == charsInS:
            return True
        else:
            return False