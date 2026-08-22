def fun(j, temp, phone, digits,ans):
    if j >= len(digits):
        ans.append(temp)
        return
    ip = digits[j]
    for ch in phone[ip]:
        op = temp + ch
        print(ip, op, ans)
        fun(j + 1, op, phone, digits,ans)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }
        ans =[]
        fun(0,"",phone,digits,ans)
        return ans