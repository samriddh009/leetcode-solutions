#input output approach 
def fun(nums,temp,ans):
    ans.append(temp)
    if not nums:
        return 
    for i in range(len(nums)):
        if i>0 and nums[i] ==nums[i-1] :
            continue
        ip = nums.copy()
        op = temp +[nums[i]]
        del ip[:i+1]
        fun(ip,op,ans)
    return ans
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # res = [[]]
        # for i in nums:
        #     res += [curr + [i] for curr in res]
        # return list(set(tuple(x) for x in res))
        nums.sort()
        ans = []
        fun(nums,[],ans)
        return ans