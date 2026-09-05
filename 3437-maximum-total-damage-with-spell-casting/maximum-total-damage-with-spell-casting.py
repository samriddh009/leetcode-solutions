@cache
def fun(i,powers,count):
    if i>=len(powers):
        return 0
    take = powers[i]*count[i]
    j = i+1
    while j<len(powers) and powers[j]<=powers[i]+2:
        j+=1
    c1 = take + fun(j,powers,count)
    c2 = fun(i+1,powers,count)
    return max(c1,c2)
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        powers = sorted(set(power))
        d = Counter(power)
        count = tuple(d[x] for x in powers)
        return fun(0,tuple(powers),count)