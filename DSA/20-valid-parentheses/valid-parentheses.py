class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}":"{", "]":"["}
        for i in s:
            if i in mapping.keys():
                if len(stack) == 0 or stack[-1] != mapping.get(i):
                    return False
                elif stack[-1] == mapping.get(i):
                    stack.pop()
            elif i in mapping.values():
                stack.append(i)
        return not stack