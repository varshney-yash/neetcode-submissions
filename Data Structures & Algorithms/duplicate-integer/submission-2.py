class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for i in nums:
            hm[i] = hm.get(i,0) + 1
        for k,v in hm.items():
            if v>1:
                return True
        return False