class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        push = ['[', '{', '(']
        stack = []
        mapping = {}
        mapping["{"] = "}"
        mapping["("] = ")"
        mapping["["] = "]"
        
        # [(])
        for char in s:
            if char in push:
                stack.append(char)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if mapping[popped] != char:
                    return False
        
        if stack:
            return False

        return True