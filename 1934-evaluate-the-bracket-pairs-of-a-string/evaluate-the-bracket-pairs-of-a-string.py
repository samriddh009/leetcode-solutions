class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = defaultdict(str)
        for i in knowledge:
            d[i[0]]=i[1]
        res = []
        stack = []
        in_bracket = False
        for char in s:
            if char == "(":
                in_bracket = True
                stack = []
            elif char == ")":
                in_bracket = False
                key = "".join(stack)
                res.append(d.get(key, "?"))
            else:
                if in_bracket:
                    stack.append(char)
                else:
                    res.append(char)
        return "".join(res)