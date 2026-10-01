class Solution(object):
    def isValid(self, s):
        stack = []
        dictionary = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in dictionary.values():
                stack.append(i)
            elif i in dictionary.keys():
                if len(stack) == 0 or stack[-1] != dictionary[i]:
                    return False
                stack.pop()
        return len(stack)==0
        