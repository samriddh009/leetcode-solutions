class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        res =[]
        for i in range(len(s)):
            if s[i]=='(' or 'a'<=s[i]<='z':
                stack.append(s[i])
            else:
                while stack and stack[-1]!='(':
                    x = stack.pop()
                    if x!='(':
                        res.append(x)
                stack.pop()
                stack.extend(res)
                res = []
        return ''.join(stack)