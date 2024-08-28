class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # created stack for opened brackets
        mapping = {")": "(", "}": "{", "]": "["}  # created map
        for i in s:
            if i in mapping.values():  # if i is opener we append to stack
                stack.append(i)
            # if i is closer we see if stack has opened that exact bracket
            elif i in mapping.keys():
                # if stack has that same exact bracket open close it
                if not stack or mapping.get(i) != stack.pop():
                    # if not opened any bracket or that same exact bracket then return False
                    return False
        return not stack

