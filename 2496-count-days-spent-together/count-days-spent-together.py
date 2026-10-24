class Solution:
    def countDaysTogether(self, a_arr: str, a_leave: str, b_arr: str, b_leave: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def f(d):
            m, day = map(int, d.split('-'))
            return sum(days[:m - 1]) + day
        
        start = max(f(a_arr), f(b_arr))
        end = min(f(a_leave), f(b_leave))
        
        return max(0, end - start + 1)