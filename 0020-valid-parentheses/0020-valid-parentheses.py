class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        for i in s:
            if i == ")":
                if len(my_stack) == 0:
                    return False
                if my_stack[-1] != "(":
                    return False
                else:
                    my_stack.pop()
            elif i == "]":
                if len(my_stack) == 0:
                    return False
                if my_stack[-1] != "[":
                    return False
                else:
                    my_stack.pop()
            elif i == "}":
                if len(my_stack) == 0:
                    return False
                if my_stack[-1] != "{":
                    return False
                else:
                    my_stack.pop()
            else:
                my_stack+=i
        if len(my_stack) == 0:
            return True
        else:
            return False