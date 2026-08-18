#input output approach 
def fun(nums,temp,ans):
    d = {}
    ans.append(temp)
    if not nums:
        return 
    for i in range(len(nums)):
        if nums[i] in d:
            continue
        d[nums[i]] = 1
        ip = nums.copy()
        op = temp +[nums[i]]
        del ip[:i+1]
        fun(ip,op,ans)
    return ans
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # res = [[]]
        # for i in nums:
        #     res += [curr + [i] for curr in res]
        # return list(set(tuple(x) for x in res))
        ans = []
        fun(nums,[],ans)
        return ans