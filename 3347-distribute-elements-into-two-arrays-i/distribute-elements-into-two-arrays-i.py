class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        i = 0
        j = 0
        arr1.append(nums[0])
        arr2.append(nums[1])
        for num in range(2,len(nums)):
            if arr1[i]>arr2[j]:
                arr1.append(nums[num])
                i+=1
            else:
                arr2.append(nums[num])
                j+=1
        return arr1+arr2