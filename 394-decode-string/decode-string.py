def fun(i: int, k: int, curr_str: str, s: str):
    if i >= len(s):
        return curr_str, i
    char = s[i]
    if char.isdigit():
        return fun(i + 1, k * 10 + int(char), curr_str, s)
    elif char == '[':
        inner_str, next_i = fun(i + 1, 0, "", s)
        return fun(next_i + 1, 0, curr_str + k * inner_str, s)
    elif char == ']':
        return curr_str, i
    else:
        return fun(i + 1, k, curr_str + char, s)
class Solution:
    def decodeString(self, s: str) -> str:
        ans, _ = fun(0, 0, "", s)
        return ans