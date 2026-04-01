class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = { '[' : ']', '{' : '}', '(' : ')'}

        for c in s:
            if c in openToClose:
                stack.append(c)
            else:
                if stack and c == openToClose[stack[-1]]:
                    stack.pop()
                else:
                    return False


        return True if len(stack) == 0 else False