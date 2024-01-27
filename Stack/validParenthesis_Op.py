class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }
        stack = []
        for char in s:
            if char in