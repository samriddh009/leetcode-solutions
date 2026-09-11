@cache
def fun(i,days,costs):
    if i>=len(days):
        return 0
    c1 = costs[0]+fun(i+1,days,costs)
    j = 0
    while j<len(days) and days[j]<days[i]+7:
        j+=1
    c2 = costs[1]+fun(j,days,costs)
    j = 0
    while j<len(days) and days[j]<days[i]+30:
        j+=1
    c3 = costs[2]+fun(j,days,costs)
    return min(c1,c2,c3)
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        return fun(0,tuple(days),tuple(costs))