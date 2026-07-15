class Solution:
    def isValid(self, s: str) -> bool:
        if "{" in s and "}" not in s:
            return False
        elif "[" in s and "]" not in s:
            return False
        elif "(" in s and ")" not in s:
            return False
        else:
            return True