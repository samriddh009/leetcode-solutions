class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(10):
            x = self.prod(n+i)
            if x%t==0:
                return n+i
    def prod(self,j):
        product = 1
        while j > 0:
            digit = j % 10
            product *= digit
            j //= 10
        return product  