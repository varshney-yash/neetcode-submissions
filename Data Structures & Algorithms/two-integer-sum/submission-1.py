class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        ans = []
        for idx,num in enumerate(nums):
            d[num] = idx
        for idx,num in enumerate(nums):
            if(target-num) in d.keys() and d[target-num]!=idx:
                ans.append(idx)
                ans.append(d[target-num])
                return ans
        return -1

                