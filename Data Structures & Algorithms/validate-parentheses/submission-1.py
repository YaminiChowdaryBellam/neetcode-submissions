class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mydict = {
            "(":")",
            "{":"}",
            "[":"]"
        }

        for value in s:
            if value in ["{","[","("]:
                stack.append(value)
                
            else:
                if stack:
                    if value != mydict[stack[-1]]:
                        return False
                    stack.pop()
                else:
                    return False

        if stack:
            return False
        return True
            


