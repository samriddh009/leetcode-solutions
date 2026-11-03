class Solution:
    def minMoves(self, nums: List[int]) -> int:
        moves = 0
        m= max(nums)
        for i in nums:
            moves+=-i+m
        return moves