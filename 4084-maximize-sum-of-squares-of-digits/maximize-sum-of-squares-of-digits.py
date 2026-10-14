class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum>num*9 or sum<1:
            return ""
        digits =[]
        remaining = sum
        for i in range(num):
            if remaining >=9:
                digits.append(9)
                remaining -= 9
            elif remaining >0:
                digits.append(remaining)
                remaining = 0
            else:
                digits.append(0)
        result =""
        for digit in digits:
            result += str(digit)
        return result