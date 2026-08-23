class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        #trick to calulate smallest prime factor
        max_n = max(nums)
        p_facts = list(range(max_n+1))
        for i in range(2,int(max_n**0.5)+1):
            if p_facts[i] == i:
                for j in range(i*i,max_n+1,i):
                    if p_facts[j] == j:
                        p_facts[j] = i
        #all prime factors calculate karne hain 
        #usme upar vali trick se spf liye 
        facts = []
        for i in nums:
            tmp = i
            cur = []
            while tmp>1:
                #"prime" factors directly nahi bana sakte bahut saare honge, shortcut sochna hoga
                j = p_facts[tmp]
                cur.append(j)
                while tmp%j==0:
                    tmp //=j
            facts.append(cur)
        d ={}
        low = 0
        ans = 0
        for high in range(n):
            #yahan abhi factors lane hain
            for i in facts[high]:
                d[i]= d.get(i,0)+1
            while len(d)>k:
                for i in facts[low]:
                    d[i] -=1
                    if d[i] ==0:
                        del d[i]
                low+=1
            ans = max(ans,high-low+1)
        return ans