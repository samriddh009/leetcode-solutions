class Solution:
  def maxAlternatingSum(self, nums: List[int]) -> int:
    squares = sorted(x * x for x in nums)
    n = len(squares)
    mid = n // 2
    ans = sum(squares[mid:]) - sum(squares[:mid])
    return ans