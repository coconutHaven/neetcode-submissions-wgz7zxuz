class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magCount = {}

        for c in magazine:
            if c in magCount:
                magCount[c] += 1
            else:
                magCount[c] = 1
        
        for c in ransomNote:
            if c not in magCount or magCount[c] <= 0:
                return False
            else:
                magCount[c] -= 1
        
        return True