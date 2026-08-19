class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        d = defaultdict(list)
        for key, value in reservedSeats:
            d[key].append(value)
        valid_seats = [{2,3,4,5},{4,5,6,7},{6,7,8,9}]
        ans = (n - len(d)) * 2
        for occupied in d.values():
            occupied = set(occupied)
            l_free = not (valid_seats[0] & occupied)
            m_free = not (valid_seats[1] & occupied)
            r_free = not (valid_seats[2] & occupied)
            if l_free and r_free:
                ans += 2
            elif l_free or m_free or r_free:
                ans += 1
        return ans