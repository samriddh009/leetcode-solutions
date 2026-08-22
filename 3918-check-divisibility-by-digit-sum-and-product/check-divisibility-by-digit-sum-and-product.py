def digit_sum(n):
    if n ==0:
        return 0
    return n%10+digit_sum(n//10)
def digit_prod(n):
    if n==0:
        return 1
    return n%10*digit_prod(n//10)
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x = digit_sum(n)
        y = digit_prod(n)
        print(x,y)
        if n %(x+y)==0:
            return True
        return False