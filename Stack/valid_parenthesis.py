class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack:
                    return False
                current_char = stack.pop()
                if current_char == '(' and char != ')':
                    return False
                if current_char == '{' and char != '}':
                    return False
                if current_char == '[' and char != ']':
                    return False

        return True

solution = Solution()
print(solution.isValid('({[]})'))
