class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        period_support = []
        preding_element = []
        for char in range(len(s)):
            if char == '.':
                period_support += s[char]
                return True
            elif char == '*' and s[char-1]:
                preding_element += s[char]
                return True
            return False
                