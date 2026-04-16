class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        push = ['(', '[', '{']

        mapping = {}
        mapping['('] = ')'
        mapping['{'] = '}'
        mapping['['] = ']'

        for c in s:
            if c in push:
                stack.append(c)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if mapping[popped] is not c:
                    return False
        if stack:
            return False
        return True