class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        n = len(position)
        p1 = position[-1]
        v1 = speed[-1]
        count=1
        for i in range(n-2,-1,-1):
            d = p1 - position[i]
            if d<=distance or v1<speed[i]:
                p1 = position[i]
                continue
            count+=1
            p1 = position[i]
            v1 = speed[i]
        return count